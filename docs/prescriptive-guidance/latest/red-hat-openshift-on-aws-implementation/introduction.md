---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/introduction.html
---

# Red Hat OpenShift on AWS implementation strategies
<a name="introduction"></a>

*Yogesh Bhatia and Francis Nelson, Amazon Web Services*

This guide provides an overview of the Red Hat OpenShift architecture on AWS, describes different methods for setting up a Red Hat OpenShift cluster, and explains the advantages and disadvantages of each method.

Red Hat OpenShift was initially used as a private cloud platform that provides a platform as a service (PaaS) for on-premises applications. Overall cluster management is handled by an in-house team that provides support to internal stakeholders, especially developers. However, managing an entire cluster on premises can become complex and might not be a scalable solution for the long term.

Red Hat OpenShift on AWS enables you to provision an entire infrastructure on AWS. It provides scalability and flexibility, so your teams can focus on using Red Hat OpenShift services instead of setting up or configuring the services. Red Hat OpenShift architecture can become complex and has many infrastructure component requirements, so coming up with the most optimal solution and architecture is key. This guide covers various options for setting up Red Hat OpenShift on AWS. It provides you with the information that you need to:
+ Create a detailed topology and architecture before provisioning a Red Hat OpenShift cluster on AWS.
+ Gain a thorough understanding of the different installation approaches, and the advantages and disadvantages of each approach.
+ Provision a Red Hat OpenShift cluster on AWS infrastructure successfully, and get all required resources up and running.

## About Red Hat OpenShift
<a name="about-rosa"></a>

Red Hat OpenShift is a wrapper to Kubernetes that provides a cloudlike experience for container management. It extends the capabilities of Kubernetes and provides its own API layer and additional benefits such as the [Source-to-Image (S2I)](https://access.redhat.com/documentation/en-us/openshift_container_platform/3.7/html-single/architecture/index#source-build) build method and ease of assigning [role-based access control (RBAC)](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.1/html/authentication/using-rbac) to namespaces. Red Hat OpenShift is used with other Red Hat products such as Ansible and Red Hat Linux to provide cluster management and operational services. Red Hat OpenShift includes Kubernetes for container orchestration. It also includes other software services such as Tekton, Grafana, CRI-O, and Prometheus, which give you the ability to manage production-grade clusters. These products and services work together in a distributed environment to provide a seamless orchestration engine experience. For more information about Red Hat OpenShift, see the [Red Hat documentation](https://www.redhat.com/en/technologies/cloud-computing/openshift).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
