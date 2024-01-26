# Changelog

<!--next-version-placeholder-->

## Release v1.0.0 (01/13/2024)

### Feedback on Milestone 1 ([issue #]())

Following up on the feedback from Grapescope for Milestone 1, this issue serves as a checklist to guide our revisions for Milestone 4. Let's ensure we address the necessary and related points to avoid repeating any deductions.

**1. Software package project structure**: There is a section in the README that outlines the planned package but it is missing some expected information. - All of the functions wrap around existing Altair options - README needs more information on how this EDA package is distinct from Altair and their available plots: https://altair-viz.github.io/gallery/index.html

**2. Function design (planned)**: Critical parameters need to be more specifically defined for all functions. “Cols: A list of column names in the dataframe to be included in the histogram” is not sufficient -- which column goes on the x axis? which goes on the y axis? what happens if you feed in 10 column names? Could be better to split into two parameters, x and y, instead.

**3. GitHub project board**: Rather than have a single issue called "Milestone 1" which lists out all the specific tasks in the discussion as a giant checklist/to-do list, you should be splitting out the tasks as separate issues and assigning them individually to group members. Otherwise, it is hard to keep track of who is responsible for what specific tasks and to use the project board to move tasks from to do > in progress > done.

**4. Follows GitHub flow version control workflow**:  - Division of work on many branches is not ideal (branches are too big - they should be small independent units of work). - Many contributions did not go through code review via a pull-request.

**5. GitHub release**: Release name mildly deviates from instructions on how to name it. Tiff's comments about version # on course Slack channel: "0.1.0 means new features, and because there is not a 1 in the first digit it means it is quite "new" and maybe not a completely done version of the project. That suits where we land we get a first working version of a package. 1.0.0 is a major version release and indicates breaking changes to a project (meaning it is not backwards compatible)."

**6. GitHub issues for communication**: GitHub issues were used somewhat for project communication.

### 🚀Implemented Enhancements

- Feedback 1: Updated README includes a comprehensive comparison and explanation of our package's unique features and functionalities, alongside how it complements and differs from Altair's offerings. Please see this [commit]() for details.
- Feedback 2: Refined the parameter design in our functions, ensuring critical parameters like `cols` are explicitly defined for enhanced clarity. Now, parameters are distinctly separated into `x` and `y` to specify the respective axes, offering a more intuitive and error-resistant interface. The refinements are refected in this [commit](). 

### 🗑️Deprecations and Removals

- Feedback 4: We now ensure that useless and irrelated branches have been removed, and remaining branches are independent unit of work, facilitating better organization and efficiency. The active branches are listed [here](https://github.com/UBC-MDS/doeasyeda/branches).

### 💬Comments and Acknowledgements

- Feedback 3: We wanted to share that Milestone 1 was completed collaboratively during a lab session, which occurred prior to the introduction of the project board tool in our course. This synchronous collaboration led us to manage the tasks internally without the need for separate issue tracking at that stage. However, we completely agree with the benefits of using GitHub's project board to enhance visibility and accountability within the team. With this in mind, we make sure that we implemented this approach for Milestone 2 and future milestones.
- Feedback 5: Rregarding the versioning of GitHub releases, as well as Tiff's valuable insights shared on the Slack channel. we understand the importance of adhering to semantic versioning standards and appreciate the clarity provided on the subject. We acknowledge that our recent release of milestone 1 naming, "1.0.0", was an oversight on our part and not in full alignment with the conventional guidelines outlined for version numbers. This was an inadvertent step before we were fully aware of the recommended practices. Having already utilized "2.1.0" for our Milestone 2 release, we aim to maintain consistency for the upcoming Milestone 3, which will, therefore, be versioned as "2.2.0". This will help avoid any confusion and keep a sequential order in our release history.
- Feedback 6:


## Release v2.1.0 (01/20/2024)

### Feedback on Milestone 2 ([issue #]())

### 🚀Implemented Enhancements


### 🗑️Deprecations and Removals


### 💬Comments and Acknowledgements



### Feedback from Peer Review ([issue #]())

#### Review Comments:

### 🚀Implemented Enhancements



### 🗑️Deprecations and Removals



### 💬Comments and Acknowledgements



## Notes

* Each entry in this log is intended to make tracking changes and their reasons transparent and straightforward.
* The log is maintained consistently to ensure that every significant modification, addition, or removal is documented for easy reference.
