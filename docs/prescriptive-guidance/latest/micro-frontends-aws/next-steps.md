---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/next-steps.html
---

# Next steps
<a name="next-steps"></a>

This guide covered architectural and organizational patterns, trade-offs for key decisions, and governance concerns related to micro-frontends. The tables summarize the trade-offs of practices discussed in this document in terms of the following dimensions:
+ **Autonomy** ‒ Each micro-frontend team's ability to independently evolve their implementation and release to end users.
+ **Consistency** ‒ The overall experience of the application where each micro-frontend behaves as expected. High consistency means micro-frontends are consistent with the rest of the application and are not detrimental to the user experience of the overall application.
+ **Complexity** ‒ The amount of infrastructure, code, and effort required to implement and test micro-frontends, the overall application, and governance controls.

|
|
| Practice | Autonomy | Consistency | Complexity |
| --- |--- |--- |--- |
| **Building with micro-frontends instead of monolithic applications** | High | Medium | High |

|
|
| Code-sharing practices | Autonomy | Consistency | Complexity |
| --- |--- |--- |--- |
| Share nothing | High | Low | Low |
| Share cross-cutting concerns | Medium | High | Medium |
| Share business logic | Low | High | Medium |
| Share through libraries at build time | Medium | High | Low |
| Share at runtime | High | High | High |

|
|
| Micro-frontend discovery practices | Autonomy | Consistency | Complexity |
| --- |--- |--- |--- |
| Configure during application build | Low | High | Low |
| Server-side discovery | High | High | Medium |
| Client-side (runtime) discovery | High | High | Medium |

|
|
| View composition practices | Autonomy | Consistency | Complexity |
| --- |--- |--- |--- |
| Server-side composition | High | Medium | High |
| Edge-side composition | Medium | Medium | High |
| Client-side composition | High | Medium | Medium |

To learn more about the concepts introduced in this guidance, see the [Resources](resources.md) section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
