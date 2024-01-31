import altair as alt
import pandas as pd
import pytest
from unittest.mock import patch

from doeasyeda.create_line_plot import create_line_plot, DoEasyEDAException


def test_line_plot_successful_plot_creation():
    """
    Test if the line plot is successfully created with valid input data.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    chart = create_line_plot(df, 'x', 'y')
    assert isinstance(chart, alt.Chart)


def test_line_plot_empty_dataframe():
    """
    Test the line plot creation with an empty DataFrame.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="Empty dataframe received!"):
        create_line_plot(df, 'x', 'y')


def test_line_plot_invalid_column_names():
    """
    Test the line plot creation with invalid column names.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    with pytest.raises(ValueError):
        create_line_plot(df, 'x', 'y')


def test_line_plot_with_width_and_height():
    """
    Test the line plot creation with specified width and height.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    width, height = 400, 300
    chart = create_line_plot(df, 'x', 'y', width=width, height=height)

    chart_dict = chart.to_dict()
    assert chart_dict['width'] == width
    assert chart_dict['height'] == height


def test_line_plot_with_title():
    """
    Test the line plot creation with a specified title.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    title = "Test line Plot"
    chart = create_line_plot(df, 'x', 'y', title=title)

    chart_dict = chart.to_dict()
    assert chart_dict['title'] == title


def test_line_plot_with_color():
    """
    Test the line plot creation with color.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6], 'z': ['red', 'green', 'blue']})
    chart = create_line_plot(df, 'x', 'y', color='z')

    assert chart.encoding['color'].shorthand == 'z'


def test_line_plot_with_tooltip():
    """
    Test the line plot creation with tooltip.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6], 'z': ['red', 'green', 'blue']})
    chart = create_line_plot(df, 'x', 'y', tooltip=['z'])

    assert chart.encoding['tooltip'][0].shorthand == 'z'


def test_line_plot_with_linteractive():
    """
    Test the line plot creation with interactive.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    chart = create_line_plot(df, 'x', 'y', interactive=True)

    assert chart.interactive


def test_do_easy_eda_exception():
    # Create a sample dataframe
    df = pd.DataFrame({'x': [1, None, 3], 'y': [None, 5, 6]})

    with patch('doeasyeda.create_line_plot.alt.Chart') as mock_chart:
        mock_chart.side_effect = Exception("Test Exception")
        
        with pytest.raises(DoEasyEDAException):
            create_line_plot(df, 'x', 'y')

