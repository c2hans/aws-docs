---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/preparation.html
---

# Preparing to build an internal developer platform
<a name="preparation"></a>

## Building your platform engineering team
<a name="platform-engineering-team"></a>

Your internal developer platform journey starts by building your platform engineering team. As described in [Principles of building an internal developer platform](principles.md), this team is responsible for build platform capabilities by following a product mindset approach. They help developers adopt the platform capabilities and make sure that these capabilities meet their requirements. This includes creating a feature roadmap for the platform and prioritizing feature development.

Your platform engineering team, as a whole, needs to have the following skillset:
+ **Development** – Create web user interfaces, command-line interfaces, or any additional layers of abstraction so that developers can interact with the internal developer platform.
+ **Operations** – Create dashboards, metrics, and alerts that address different observability pillars after deploying the workloads.
+ **Automation and infrastructure as code (IaC)** – Design golden paths and develop any templates that automate the different stages in the SDLC, including the tools and infrastructure used to serve the workloads.
+ **Security** – Establish security scanning and policy-as-code mechanisms that provide a governance framework to help protect workloads.

For more information about how a platform engineering team fits within your organization, see the [model](https://teamtopologies.com/infographic/getting-started-with-team-topologies-infographic) on the Team Topologies website. In addition, see [Platform Engineer & Application Developer Organizational Models](https://github.com/aws/aws-proton-public-roadmap/issues/66) on GitHub.

## Planning your platform journey
<a name="planning-your-journey"></a>

After building your platform engineering team, you define your internal developer platform journey. The final goal of the internal developer platform is to provide self-service capabilities that developers can easily use. You can achieve this by adopting a product mindset and following a well-defined process. Your platform engineering team should perform the following general steps to develop your internal developer plan:

1. Identify the areas of cognitive load and what can be automated. Ask questions such as the following:
   + How do you get the state of the entire system?
   + How do you debug and remediate issues?
   + How do you pass secrets from one pipeline to another?
   + How do you delete all unused resources?

1. Inventory all of the existing tools, systems, and processes that your developers use. The goal is to move to a more centralized approach that can scale to serve different experiences and more teams.

1. Identify a single golden path, and create a template to automate as much as possible, from environment creation to observability.

1. As you develop the golden path, identify all of the security guardrails that can be automated in the golden path. Align the golden path with your organization's compliance requirements.

1. After the internal developer platform is available, enable the use of this golden path. Start to build a self-service mechanism that developers can use, such as a web user interface, a command-line interface, or an API.

For more information, see the following AWS blog posts:
+ [How to Set Up a Platform That Effectively Supports Your Development Teams](https://aws.amazon.com/blogs/enterprise-strategy/how-to-set-up-a-platform-that-effectively-supports-your-development-teams/)
+ [Delivering Business Value with Cloud Platform Teams](https://aws.amazon.com/blogs/mt/delivering-business-value-with-cloud-platform-teams/)
