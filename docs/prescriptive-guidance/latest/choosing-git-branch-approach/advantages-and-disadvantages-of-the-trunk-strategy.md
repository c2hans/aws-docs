---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/advantages-and-disadvantages-of-the-trunk-strategy.html
---

# Advantages and disadvantages of the Trunk strategy
<a name="advantages-and-disadvantages-of-the-trunk-strategy"></a>

The Trunk branching strategy is well suited for smaller, mature, development teams that have strong communication skills. It also works well if you have continuous, rolling feature releases for the application. It is not well suited if you have large or fragmented development teams or if you have expansive, scheduled feature releases. Merge conflicts will occur in this model, so be aware that resolution of merge conflicts is a key skill. All team members must be trained accordingly.

## Advantages
<a name="advantages"></a>

Trunk-based development offers several advantages that can improve the development process, streamline collaboration, and enhance the overall quality of the software. The following are some of the key benefits:
+ **Faster feedback loops** – With trunk-based development, developers integrate their code changes frequently, often multiple times a day. This enables faster feedback regarding potential issues and helps developers identify and fix problems more quickly than they would in a feature-based development model.
+ **Reduced merge conflicts** – In trunk-based development, the risk of large, complicated merge conflicts is minimized because changes are integrated continuously. This helps maintain a cleaner code base and reduces the amount of time spent resolving conflicts. Resolving conflicts can be both time-consuming and error-prone in feature-based development.
+ **Improved collaboration** – Trunk-based development encourages developers to work together on the same branch, promoting better communication and collaboration within the team. This can lead to faster problem-solving and a more cohesive team dynamic.
+ **Easier code reviews** – Because code changes are smaller and more frequent in trunk-based development, it can be easier to conduct thorough code reviews. Smaller changes are generally easier to understand and review, leading to more effective identification of potential issues and improvements.
+ **Continuous integration and delivery** – Trunk-based development supports the principles of continuous integration and continuous delivery (CI/CD). By keeping the code base in a releasable state and integrating changes frequently, teams can more easily adopt CI/CD practices, which leads to faster deployment cycles and improved software quality.
+ **Enhanced code quality** – With frequent integration, testing, and code reviews, trunk-based development can contribute to better overall code quality. Developers can catch and fix issues more quickly, reducing the likelihood of technical debt accumulating over time.
+ **Simplified branching strategy** – Trunk-based development simplifies the branching strategy by reducing the number of long-lived branches. This can make it easier to manage and maintain the code base, especially for large projects or teams.

## Disadvantages
<a name="disadvantages"></a>

Trunk-based development does have some disadvantages, which can impact the development process and the team dynamics. The following are a few notable drawbacks:
+ **Limited isolation** – Because all developers work on the same branch, their changes are immediately visible to everyone on the team. This can lead to interference or conflicts, causing unintended side effects or breaking the build. In contrast, feature-based development isolates changes better so that developers can work more independently.
+ **Increased pressure on testing** – Trunk-based development relies on continuous integration and automated testing to catch issues quickly. However, this approach can put a lot of pressure on the testing infrastructure and requires a well-maintained test suite. If the tests aren't comprehensive or reliable, it can lead to undetected issues in the main branch.
+ **Less control over releases** – Trunk-based development aims to keep the code base in a continuously releasable state. While this can be advantageous, it might not always be suitable for projects with strict release schedules or those that require specific features to be released together. Feature-based development provides more control over when and how features are released.
+ **Code churn** – With developers constantly integrating changes into the main branch, trunk-based development can lead to increased code churn. This can make it difficult for developers to keep track of the current state of the code base and might cause confusion when trying to understand the effect of recent changes.
+ **Requires a strong team culture** – Trunk-based development demands a high level of discipline, communication, and collaboration among team members. This can be challenging to maintain, particularly in larger teams or when working with developers who are less experienced with this approach.
+ **Scalability challenges** – As the size of the development team grows, the number of code changes being integrated into the main branch can increase rapidly. This can lead to more frequent build breaks and test failures, making it difficult to keep the code base in a releasable state.
