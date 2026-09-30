---
source_url: https://docs.aws.amazon.com/solutions/event-driven-application-autoscaling-with-keda-on-amazon-eks/index.html
---

---
title: 'Guidance for Event-Driven Application Autoscaling with KEDA on Amazon EKS'
canonical_url: https://docs.aws.amazon.com/solutions/event-driven-application-autoscaling-with-keda-on-amazon-eks/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Event-Driven Application Autoscaling with KEDA on Amazon EKS

Integrate KEDA with a Kubernetes cluster to achieve event-driven scalability

## Overview

This Guidance demonstrates how to implement event-driven autoscaling for Amazon Elastic Kubernetes Service (Amazon EKS) applications using Kubernetes Event-Driven Autoscaler (KEDA). The Guidance shows how to scale deployments based on custom metrics, rather than solely CPU and memory utilization. KEDA integrates with Kubernetes, extending autoscaling capabilities for event-driven workloads. By following this Guidance, you can optimize resource provisioning, improve cost efficiency, and enhance the customer experience for your event-driven applications on Amazon EKS using custom metrics-based autoscaling with KEDA.

## How it works

### EKS Cluster

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/event-driven-application-autoscaling-with-keda-on-amazon-eks.pdf?target=_blank)Step 1Set up an AWS Cloud9 environment with AWS Identity and Access Management (IAM) permissions.Step 2Install helm, eksctl, kubectl, and AWS Command Line Interface (CLI) in AWS Cloud9.Step 3Amazon Elastic Kubernetes Service (Amazon EKS) cluster and EKS managed node groups are launched through AWS Cloud9.Step 4KEDA is deployed with the required IAM role for service account (IRSA).Step 5Deploy Amazon Simple Queue Service (Amazon SQS) to decouple communication between applications and attach a policy on KEDA IRSA to access Amazon SQS.Step 6Create Amazon Managed Service for Prometheus and optionally, Amazon Managed Grafana.Step 7Configure AWS Distro for OpenTelemetry to send application metrics to Amazon Managed Service for Prometheus, deployed with the required IAM IRSA.Step 8Configure the Sigv4 proxy pod to authenticate KEDA with Amazon Managed Service for Prometheus, deployed with the required IAM IRSA.### KEDA Overview

This architecture diagram shows an overview of how KEDA, the Kubernetes Horizontal Pod Autoscaler (HPA), and external event sources work together. For KEDA scaling pods, open the next tab.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/event-driven-application-autoscaling-with-keda-on-amazon-eks.pdf#page=2)Step 1The scaled object is a CustomResourceDefinition (CRD) to configure the event source, deployment to be scaled, and scaling behavior.Step 2KEDA activates and deactivates Kubernetes deployments to scale to and from zero on no events. This is one of the primary roles of the keda-operator container that runs when you install KEDA.Step 3KEDA feeds custom metrics for Kubernetes Horizontal Pod Autoscaling (HPA) to scale from one to the required amount of pods.Step 4HPA scales the pods based on KEDA instructions.Step 5KEDA supports more than 60 event sources, available at: Currently available scalers for KEDA.### Scaling with KEDA

This architecture diagram shows KEDA scaling deployment pods based on custom metrics sources. For the EKS cluster, open the first tab.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/event-driven-application-autoscaling-with-keda-on-amazon-eks.pdf#page=3)Step 1The app uses Amazon SQS to decouple communication between microservicesStep 2AWS Distro for OpenTelemetry gets metrics from the application and sends them to Amazon Managed Service for Prometheus.Step 3KEDA is configured to use Amazon SQS and the Amazon Managed Service for Prometheus scaler to get Amazon SQS queue length and Prometheus custom metrics.Step 4KEDA (keda-operator-metrics-apiserver) exposes event data for HPA to scale.Step 5HPA scales to the appropriate number of pods.Step 6Cluster Autoscaling (CA) provisions the required nodes using auto scaling group. Instead of CA, you can also use Karpenter.Step 7New capacity is provisioned as required.Step 8You can optionally configure Amazon Managed Grafana to show metrics from Amazon Managed Service for Prometheus in a dashboard.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/event-driven-application-autoscaling-with-keda-on-amazon-eks.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-event-driven-application-auto-scaling-with-keda-on-amazon-eks)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This event-driven architecture allows you to define precise scaling rules, granting fine-grained control over how your applications respond to specific events or metrics. By using KEDA, you can enhance the efficiency, resource utilization, and responsiveness of your Kubernetes environment, driving operational excellence. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Use IAM roles to obtain temporary credentials, enabling access to diverse AWS services. For your Kubernetes-based applications, integrate with native authentication and authorization mechanisms to securely interact with the Kubernetes API server. By precisely defining IAM policies to grant the minimal necessary permissions, you effectively mitigate unauthorized access and strengthen the security of your environment. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Using pod topology spread constraints in Kubernetes can help you bolster availability and resilience of your applications. This feature enables you to control the distribution of your pods across different failure domains, such as hosts or Availability Zones. By ensuring a balanced and optimal spread, you minimize the impact of potential failures within a single domain, enhancing the overall integrity of your application. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The Amazon EKS cluster's multi-Availability Zone setup allows for low-latency performance. While inter-subnet traffic across Availability Zones may occur, the resulting latency is expected to have a minimal impact on your application's performance. In scenarios where even lower latency is required, you can direct traffic within a single Availability Zone to further optimize network performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

KEDA's automated pod scaling capabilities can help provide cost savings. By using custom metrics to initiate scaling, you can support optimal pod availability to meet your application's needs, avoiding overprovisioning and unnecessary costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

You can achieve sustainable resource management through Kubernetes HPA. KEDA uses this capability to effectively scale your workloads based on custom metrics so that only the required pods run. With access to over 60 different scalers, you can tailor the scaling behavior to your specific needs, maximizing the utilization of your deployed resources and preventing overallocation. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
