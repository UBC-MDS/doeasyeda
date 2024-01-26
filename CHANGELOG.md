# Changelog

<!--next-version-placeholder-->

## Release v1.0.0 (01/13/2024)

### Feedback on Milestone 1 ([issue #]())

Following up on the feedback from Grapescope for Milestone 1, this issue serves as a checklist to guide our revisions for Milestone 4. Let's ensure we address the necessary and related points to avoid repeating any deductions.

**1. Software package project structure**: There is a section in the README that outlines the planned package but it is missing some expected information. - All of the functions wrap around existing Altair options - README needs more information on how this EDA package is distinct from Altair and their available plots: https://altair-viz.github.io/gallery/index.html

**2. Function design (planned)**: Critical parameters need to be more specifically defined for all functions. “Cols: A list of column names in the dataframe to be included in the histogram” is not sufficient -- which column goes on the x axis? which goes on the y axis? what happens if you feed in 10 column names? Could be better to split into two parameters, x and y, instead.

**3. GitHub project board**: Rather than have a single issue called "Milestone 1" which lists out all the specific tasks in the discussion as a giant checklist/to-do list, you should be splitting out the tasks as separate issues and assigning them individually to group members. Otherwise, it is hard to keep track of who is responsible for what specific tasks and to use the project board to move tasks from to do > in progress > done.

**4. Follows GitHub flow version control workflow**:  - Division of work on many branches is not ideal (branches are too big - they should be small independent units of work). - Many contributions did not go through code review via a pull-request.

**5. GitHub release**: Grading comment:Release name mildly deviates from instructions on how to name it. Tiff's comments about version # on course Slack channel: "0.1.0 means new features, and because there is not a 1 in the first digit it means it is quite "new" and maybe not a completely done version of the project. That suits where we land we get a first working version of a package. 1.0.0 is a major version release and indicates breaking changes to a project (meaning it is not backwards compatible)."

**6. GitHub issues for communication**: GitHub issues were used somewhat for project communication.

### 🚀Implemented Enhancements



### 🗑️Deprecations and Removals



### 💬Comments and Acknowledgements




## Release v2.0.0 (01/20/2024)

### Feedback on Milestone 2 ([issue #]())


### 🚀Implemented Enhancements



### 🗑️Deprecations and Removals



### 💬Comments and Acknowledgements




```
#### Documentation

The package includes all the following forms of documentation:

- [ ] **A statement of need** clearly stating problems the software is designed to solve and its target audience in README.
- [ ] **Installation instructions:** for the development version of the package and any non-standard dependencies in README.
- [ ] **Vignette(s)** demonstrating major functionality that runs successfully locally.
- [ ] **Function Documentation:** for all user-facing functions.
- [ ] **Examples** for all user-facing functions.
- [ ] **Community guidelines** including contribution guidelines in the README or CONTRIBUTING.
- [ ] **Metadata** including author(s), author e-mail(s), a url, and any other relevant metadata e.g., in a `pyproject.toml` file or elsewhere.

Readme file  requirements
The package meets the readme requirements below:

- [ ] Package has a README.md file in the root directory.

The README should include, from top to bottom:

- [ ] The package name
- [ ] Badges for:
    - [ ] Continuous integration and test coverage,
    - [ ] Docs building (if you have a documentation website),
    - [ ] A [repostatus.org](https://www.repostatus.org/) badge,
    - [ ] Python versions supported,
    - [ ] Current package version (on PyPI / Conda).

*NOTE: If the README has many more badges, you might want to consider using a table for badges: [see this example](https://github.com/ropensci/drake). Such a table should be more wide than high. (Note that the a badge for pyOpenSci peer-review will be provided upon acceptance.)*

- [ ] Short description of package goals.
- [ ] Package installation instructions
- [ ] Any additional setup required to use the package (authentication tokens, etc.)
- [ ] Descriptive links to all vignettes. If the package is small, there may only be a need for one vignette which could be placed in the README.md file.
    - [ ] Brief demonstration of package usage (as it makes sense - links to vignettes could also suffice here if package description is clear)
- [ ] Link to your documentation website.
- [ ] If applicable, how the package compares to other similar packages and/or how it relates to other packages in the scientific ecosystem.
- [ ] Citation information
```



### Feedback from Peer Review ([issue #]())

#### Review Comments: 




### 🚀Implemented Enhancements



### 🗑️Deprecations and Removals



### 💬Comments and Acknowledgements



## Notes

* Each entry in this log is intended to make tracking changes and their reasons transparent and straightforward.
* The log is maintained consistently to ensure that every significant modification, addition, or removal is documented for easy reference.
