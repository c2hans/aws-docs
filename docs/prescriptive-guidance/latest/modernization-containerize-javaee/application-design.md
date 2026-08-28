---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-containerize-javaee/application-design.html
---

# Container-based application design
<a name="application-design"></a>

## Java EE replatforming challenges
<a name="java-ee-replatforming-challenges.8a9fef8b-0f9f-5b2a-ba81-d74380942c39"></a>

You can face the following challenges when you migrate your Java EE application to a containerized platform in the AWS Cloud:
+ **Disposability **– To keep a container "stateless," you might have to store session state in an external database. Container-based applications require a faster, smaller application runtime, and your Java EE application server might not be able to run in the container environment.
+ **Container platform compatibility** – You might have to reduce application runtime-specific capabilities, such as clustering, application deployment, and memory replications.
+ **Portability** – Container-based applications are deployed by using an application runtime, while traditional Java EE applications are deployed by using application packages (.jar or .war files).

## Best practices for container-based application design
<a name="best-practices-for-container-based-application-design.a0bb0731-9a3f-5cfe-9bd7-f707915c4843"></a>

We recommend that you follow these best practices when you design your container-based Java EE applications for the AWS Cloud:
+ Avoid making changes to your container instance after you created it. If you must make changes, build a new container image and reuse that new image across all environments.
+ Avoid storing permanent data inside your container.
+ Design your container so that it addresses a single purpose.
+ Make sure that your container implements all necessary APIs.
+ Design your container so that its system requirements are built around CPU usage, system memory, and persistent storage.

For more information on best practices, see [Principles of Container-based Application Design](https://kubernetes.io/blog/2018/03/principles-of-container-app-design/) in the Kubernetes documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
