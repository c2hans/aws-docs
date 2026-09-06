---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/security.html
---

# Security
<a name="security"></a>

A fully CI/CD process provides a fully automated single source of truth approach to deployment. The pipeline has a single point of entry. Software updates enter the pipeline at the beginning and are passed as-is from one environment to the next. If an issue is discovered at any stage in the pipeline, the code changes that fix it must go through the same process and start at the first stage. Reducing the points of entry in a pipeline also reduces the possible ways that vulnerabilities can be introduced into the pipeline.

Additionally, because the entry point is the furthest possible point from the production environment, this drastically reduces the likelihood of vulnerabilities reaching production. If you implement a manual approval process in a fully CI/CD pipeline, you can still allow for go or no-go decision making about whether changes are promoted to the next environment. The decision maker is not necessarily the same person who deploys changes. This separates the responsibilities for the deployer of code changes and the approver of those changes. It also makes it more feasible for a less technical organization leader to perform the role of approver.

Finally, the single point of entry helps you limit write access to the production environment's user interface (UI) console to a few or even zero users. By reducing the number of users who can make manual changes in the console, you reduce the risk of security events. The ability to manually manage the console in the production environment is far more necessary in legacy workflows than in a CI/CD automated approach. These manual changes are more difficult to track, review, and test. They're usually performed to save time, but in the long run, they add significant technical debt to the project.

Console security issues aren't necessarily caused by bad actors. Many of the issues that occur in the console are accidental. Accidental security exposure is very common, and it has led to the rise of the zero-trust security model. This model posits, in part, that security accidents are less likely when even internal staff has as little access as possible, also known as *least-privilege permissions*. Preserving the integrity of the production environment by restricting all processes to an automated pipeline practically eliminates the risk of console-related security issues.
