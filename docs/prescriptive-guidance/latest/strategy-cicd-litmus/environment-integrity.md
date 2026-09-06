---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/environment-integrity.html
---

# Environment integrity
<a name="environment-integrity"></a>

As many developers know, one change in code can sometimes create a [butterfly effect](https://www.americanscientist.org/article/understanding-the-butterfly-effect) (American Scientist article), where a small deviation that is seemingly unrelated sets off a chain reaction that causes unexpected results. Developers must then fully investigate to discover the root cause.

When scientists conduct an experiment, they separate the test subjects into two groups: the experimental group and the control group. The intention is to make the experimental group and the control group completely identical except for the thing being tested in the experiment. When something happens in the experimental group that doesn't happen in the control group, the only cause can be the thing being tested.

Think of the changes in a deployment as the experimental group, and think of each environment as separate control groups. The results of testing in a lower environment are only reliable when the controls are the same as in an upper environment. The more the environments deviate, the greater the chance of discovering defects in the upper environments. In other words, if the code changes are going to fail in production, we'd much rather them fail in beta first so that they never get to production. This is why every effort should be made to keep each environment, from the lowest test environment to production itself, in sync. This is called *environment integrity*.

The goal of any fully CI/CD process is to discover issues as early as possible. Preserving the environment integrity by using a trunk-based approach can virtually eliminate the need for hotfixes. In a trunk-based workflow, it's rare for an issue to first appear in the production environment.

In a Gitflow approach, after a hotfix is deployed directly to upper environments, it is then added to the development branch. This preserves the fix for future releases. However, the hotfix was developed and tested directly off of the current state of the application. Even if the hotfix works perfectly in production, there's a possibility that problems will arise when it interacts with the newer features in the development branch. Because deploying a hotfix for a hotfix is not typically desirable, this leads to developers spending extra time trying to retrofit the hotfix into the development environment. In many cases, this can lead to significant technical debt and reduce the overall stability of the development environment.

When a failure occurs in an environment, all changes are rolled back so that the environment is returned to its previous state. Any change to a code base should start the pipeline over again from the very first stage. When an issue does arise in the production environment, the fix should go through the entire pipeline as well. The extra time it takes to go through the lower environments is usually negligible compared to the problems that are avoided by using this approach. Because the whole purpose of the lower environments is to catch mistakes before they reach production, bypassing these environments through a Gitflow approach is an inefficient and unnecessary risk.
