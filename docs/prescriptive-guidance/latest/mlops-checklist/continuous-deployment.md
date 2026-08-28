---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mlops-checklist/continuous-deployment.html
---

# 7. Continuous deployment
<a name="continuous-deployment"></a>

For an ML system to be continuously deployed, it must be able to divert traffic from or between live models. A continuously deployed system has at least one way by which models are promoted to production: canary, shadow, blue/green, or A/B. Confirm that in the ML system, you have at least one way to roll back models.

|  |
| --- |
| 7.1 Model switching | The system can switch between versioned models in staging and production. It can divert traffic all at once or incrementally to new production variants. |
| --- |--- |
| **7.2 Model promotion processes** | A staged validation process is in place for model promotion. The process uses offline tests that don't impact the production system, such as running against validation data in a staging environment. A runbook and metrics for model promotion are set. Promotion follows one of the rollout strategies. |
| **7.3 Rollback strategies** | A rollback strategy exists so that when an error occurs or the model deviates from expected behavior, a rollback, fallback, or roll through happens. In a rollback, the model reverts to a previous deployment version. In a fallback, the model is replaced with a strong heuristic. Roll through will promote the next model to production, rolling through the previous model. Runbooks are in place for all of these strategies. |
| **7.4 Canary deployment** | The system can deploy by using a canary. A small portion of traffic is sent to the new model initially. Over time, all traffic shifts to the new model. This shift is closely monitored because the testing happens in the production environment. |
| **7.5 Model shadow deployment** | The system can run a shadow deployment in which the new model works alongside the existing model. Both models receive traffic, but only the earlier model outputs inference. Assessments are run on the new model compared with the existing model, and then the new model is manually promoted. |
| **7.6 Blue/green deployment** | The system can deploy with a new model (green, which is staging) and the earlier model (blue, which is production), with both running at the same time. After testing is complete, traffic is diverted from the blue environment to the green one. This strategy prevents downtime because identical environments are stood up. |
| **7.7 Support for A/B testing or more** | The system supports using model versions in the deployed environment to run A/B tests on incoming traffic. This can include the ability to promote automatically based on the newer model winning in the tests. More advanced setups will use a [multi-armed bandit](https://aws.amazon.com/blogs/machine-learning/dynamic-a-b-testing-for-machine-learning-models-with-amazon-sagemaker-mlops-projects/) process. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
