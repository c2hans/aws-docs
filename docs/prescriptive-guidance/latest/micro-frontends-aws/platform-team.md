---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/platform-team.html
---

# Do you need a platform team?

Some companies have a team that owns and maintains code, infrastructure, and processes that other teams adopt to work on micro-frontends. Common responsibilities include:
+ Create and maintain a continuous integration and continuous delivery (CI/CD) pipeline that you can use with repositories containing micro-frontends. Build and test code changes, and release them in multiple environments.
+ Create and maintain observability-related tools such as shared dashboards, alerting mechanisms, and systems to react to issues.
+ Create and maintain shared libraries for event handling, shared-service consumption, and third-party dependencies.
+ Create and maintain tools that continuously monitor nonfunctional qualities such as performance, security, and reliability of the system.
+ Create and maintain design systems.
+ Create, maintain, and support the application shell for the micro-frontend system.

Depending on the scale of the project, you can manage these responsibilities by using one of the following approaches:
+ Create a dedicated platform team whose only responsibility is to work on shared tools.
+ Create a group composed of members from multiple teams. Group members split their time between working on micro-frontends and working on shared tooling. This is also known as a tiger team.

While the tiger-team approach is an effective way to stay customer focused, a tiger team often evolves into a platform team if the project gains traction and responsibilities. For both platform teams and tiger teams, many successful companies working on micro-frontends form these teams so that people with different backgrounds and skills can contribute. Team members might include backend engineers, frontend engineers, user experience (UX) designers, and technical product managers. This diversity encourages team members to engage in constructive debates and design with simplicity in mind.
