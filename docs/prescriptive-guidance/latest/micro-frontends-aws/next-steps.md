---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/next-steps.html
---

# Next steps

This guide covered architectural and organizational patterns, trade-offs for key decisions, and governance concerns related to micro-frontends. The following tables summarize the trade-offs of practices discussed in this guide across these dimensions:
+ **Autonomy** ‒ Each micro-frontend team's ability to independently evolve their implementation and release to end users.
+ **Consistency** ‒ The degree to which each micro-frontend behaves as users expect across the application. High consistency means micro-frontends align with the rest of the application and don't degrade the overall user experience.
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

To learn more about the concepts introduced in this guide, see the [Resources](resources.md) section.
