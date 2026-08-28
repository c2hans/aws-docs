---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/stage-3.html
---

# Stage 3: Evaluate and test
<a name="stage-3"></a>

During the *evaluate and test* stage of the lifecycle, the application, or changes to an existing application, have been designed but haven't yet been released to production. In this stage, you implement activities to test the practices that have been performed in previous stages and evaluate the results. The application might still be in active development, or primary development might be complete and the application might be undergoing testing before it's released to production. During this stage, you focus on developing and running tests that confirm or refute expectations that the application will meet the defined objectives for resilience. Additionally, you develop and test the system's operational procedures. The deployment procedures you developed in the [*Stage 2: Design and implement*](stage-2.md) stage are put into practice and the results are evaluated. Although these testing and evaluation activities *begin* during this portion of the lifecycle, they do not end here. Testing and evaluation continue as you move into the [*Stage 4: Operate*](stage-4.md) stage.

The *evaluate and test* stage is divided into two phases: pre-deployment activities and post-deployment activities. Pre-deployment activities consist of tasks that should be completed before you deploy the application into any environment, including deploying new versions of the software as well as the initial deployment into a testing environment. Post-deployment activities take place after the software has been deployed into a testing or production environment. The following sections discuss these phases in more detail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
