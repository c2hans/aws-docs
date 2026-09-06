---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/visual-overview-of-the-trunk-strategy.html
---

# Visual overview of the Trunk strategy
<a name="visual-overview-of-the-trunk-strategy"></a>

The following diagram can be used like a [Punnett square](https://en.wikipedia.org/wiki/Punnett_square) (Wikipedia) to understand the Trunk branching strategy. Line up the branches on the vertical axis with the AWS environments on the horizontal axis to determine what actions to perform in each scenario. The circled numbers guide you through the sequence of actions represented in the diagram. This diagram shows the development workflow of a Trunk branching strategy, from a `feature` branch in the sandbox environment to production release of the `main` branch. For more information about the activities that occur in each environment, see [DevOps environments](understanding-the-dev-ops-environments.md) in this guide.

![Punnett square of the Trunk activities in each branch and environment](http://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/images/guide-img/2c642ab1-73c3-487b-9aff-d887904354b7/images/49ff3219-e055-49a8-b19b-7b70966847d0.png)
