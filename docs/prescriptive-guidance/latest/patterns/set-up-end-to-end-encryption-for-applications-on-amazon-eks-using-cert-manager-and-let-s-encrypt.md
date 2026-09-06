---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-end-to-end-encryption-for-applications-on-amazon-eks-using-cert-manager-and-let-s-encrypt.html
---

# Set up end-to-end encryption for applications on Amazon EKS using cert-manager and Let's Encrypt
<a name="set-up-end-to-end-encryption-for-applications-on-amazon-eks-using-cert-manager-and-let-s-encrypt"></a>

*Mahendra Revanasiddappa and Vasanth Jeyaraj, Amazon Web Services*

## Summary
<a name="set-up-end-to-end-encryption-for-applications-on-amazon-eks-using-cert-manager-and-let-s-encrypt-summary"></a>

Implementing end-to-end encryption can be complex and you need to manage certificates for each asset in your microservices architecture. Although you can terminate the Transport Layer Security (TLS) connection at the edge of the Amazon Web Services (AWS) network with a Network Load Balancer or Amazon API Gateway, some organizations require end-to-end encryption.

This pattern uses NGINX Ingress Controller for ingress. This is because when you create a Kubernetes ingress, the ingress resource uses a Network Load Balancer. The Network Load Balancer doesn't permit uploads of client certificates. Therefore, you can't achieve mutual TLS with Kubernetes ingress.

This pattern is intended for organizations that require mutual authentication between all microservices in their applications. Mutual TLS reduces the burden of maintaining user names or passwords and can also use the turnkey security framework. This pattern’s approach is compatible if your organization has a large number of connected devices or must comply with strict security guidelines.

This pattern helps increase your organization's security posture by implementing end-to-end encryption for applications running on Amazon Elastic Kubernetes Service (Amazon EKS). This pattern provides a sample application and code in the GitHub [End-to-end encryption on Amazon EKS](https://github.com/aws-samples/end-to-end-encryption-on-amazon-eks#readme) repository to show how a microservice runs with end-to-end encryption on Amazon EKS. The pattern's approach uses [cert-manager](https://cert-manager.io/docs/), an add-on to Kubernetes, with [Let's Encrypt](https://letsencrypt.org/) as the certificate authority (CA). Let's Encrypt is a cost-effective solution to manage certificates and provides free certificates that are valid for 90 days. Cert-manager automates the on-demand provisioning and rotating of certificates when a new microservice is deployed on Amazon EKS.

**Intended audience**

This pattern is recommended for users who have experience with Kubernetes, TLS, Amazon Route 53, and Domain Name System (DNS).

## Prerequisites and limitations
<a name="set-up-end-to-end-encryption-for-applications-on-amazon-eks-using-cert-manager-and-let-s-encrypt-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An existing Amazon EKS cluster.
+ AWS Command Line Interface (AWS CLI) version 1.7 or later, installed and configured on macOS, Linux, or Windows.
+ The `kubectl` command line utility, installed and configured to access the Amazon EKS cluster. For more information about this, see [Installing kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) in the Amazon EKS documentation.
+ An existing DNS name to test the application. For more information about this, see [Registering domain names using Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html) in the Amazon Route 53 documentation.
+ The latest [Helm](https://docs.aws.amazon.com/eks/latest/userguide/helm.html) version, installed on your local machine. For more information about this, see [Using Helm with Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/helm.html) in the Amazon EKS documentation and the GitHub [Helm](https://github.com/helm/helm) repository.
+ The GitHub [End-to-end encryption on Amazon EKS](https://github.com/aws-samples/end-to-end-encryption-on-amazon-eks#readme) repository, cloned to your local machine.
+ Replace the following values in the `policy.json` and `trustpolicy.json` files from the cloned GitHub [End-to-end encryption on Amazon EKS](https://github.com/aws-samples/end-to-end-encryption-on-amazon-eks#readme) repository:
  + `<account number>` – Replace with the AWS account ID for the account that you want to deploy the solution in.
  + `<zone id>` – Replace with the domain name’s Route 53 zone ID.
  + `<node_group_role>` – Replace with the name of the AWS Identity and Access Management (IAM) role associated with the Amazon EKS nodes.
  + `<namespace>` – Replace with the Kubernetes namespace in which you deploy the NGINX Ingress Controller and the sample application.
  + `<application-domain-name>` – Replace with the DNS domain name from Route 53.

**Limitations **
+ This pattern doesn’t describe how to rotate certificates and only demonstrates how to use certificates with microservices on Amazon EKS.

## Architecture
<a name="set-up-end-to-end-encryption-for-applications-on-amazon-eks-using-cert-manager-and-let-s-encrypt-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Workflow to set up encryption for applications on Amazon EKS using cert-manager and Let's Encrypt.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9aa3ee9e-73db-41f5-a467-b5c47fef496e/images/40692ede-6fb3-474e-8c9e-85c51529e8ad.png)

The diagram shows the following workflow:

1. A client sends a request to access the application to the DNS name.

1. The Route 53 record is a CNAME to the Network Load Balancer.

1. The Network Load Balancer forwards the request to the NGINX Ingress Controller that is configured with a TLS listener. Communication between the NGINX Ingress Controller and the Network Load Balancer follows HTTPS protocol.

1. The NGINX Ingress Controller carries out path-based routing based on the client's request to the application service.

1. The application service forwards the request to the application pod. The application is designed to use the same certificate by calling secrets.

1. Pods run the sample application using the cert-manager certificates. The communication between the NGINX Ingress Controller and the pods uses HTTPS.

|
|
| Note: Cert-manager runs in its own namespace. It uses a Kubernetes cluster role to provision certificates as secrets in specific namespaces. You can attach those namespaces to application pods and NGINX Ingress Controller.  |
| --- |

## Tools
<a name="set-up-end-to-end-encryption-for-applications-on-amazon-eks-using-cert-manager-and-let-s-encrypt-tools"></a>

**AWS services**
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) is a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) automatically distributes your incoming traffic across multiple targets, containers, and IP addresses.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.

**Other tools**
+ [cert-manager](https://cert-manager.io/docs/installation/supported-releases/) is an add-on to Kubernetes that requests certificates, distributes them to Kubernetes containers, and automates certificate renewal.
+ [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/) is a traffic management solution for cloud‑native apps in Kubernetes and containerized environments.

## Epics
<a name="set-up-end-to-end-encryption-for-applications-on-amazon-eks-using-cert-manager-and-let-s-encrypt-epics"></a>

### Create and configure a public hosted zone with Route 53
<a name="create-and-configure-a-public-hosted-zone-with-route-53"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a public hosted zone in Route 53. | Sign in to the AWS Management Console, open the Amazon Route 53 console, choose **Hosted zones**, and then choose **Create hosted zone**. Create a public hosted zone and record the zone ID. For more information about this, see [Creating a public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html) in the Amazon Route 53 documentation.ACME DNS01 uses the DNS provider to post a challenge for cert-manager to issue the certificate. This challenge asks you to prove that you control the DNS for your domain name by putting a specific value in a TXT record under that domain name. After Let’s Encrypt gives your ACME client a token, your client creates a TXT record derived from that token and your account key, and it puts that record at `_acme-challenge.<YOURDOMAIN>`. Then Let’s Encrypt queries the DNS for that record. If it finds a match, you can proceed to issue a certificate. | AWS DevOps |

### Configure an IAM role to allow cert-manager to access the public hosted zone
<a name="configure-an-iam-role-to-allow-cert-manager-to-access-the-public-hosted-zone"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the IAM policy for cert-manager.  | An IAM policy is required to provide cert-manager with permission to validate that you own the Route 53 domain. The `policy.json` sample IAM policy is provided in the `1-IAMRole` directory in the cloned GitHub [End-to-end encryption on Amazon EKS](https://github.com/aws-samples/end-to-end-encryption-on-amazon-eks#readme) repository.<br />Enter the following command in AWS CLI to create the IAM policy.<pre>aws iam create-policy \<br />  --policy-name PolicyForCertManager \<br />  --policy-document file://policy.json</pre> | AWS DevOps |
| Create the IAM role for cert-manager. | After you create the IAM policy, you must create an IAM role. The `trustpolicy.json` sample IAM role is provided in the `1-IAMRole` directory.<br />Enter the following command in AWS CLI to create the IAM role.<pre>aws iam create-role \<br />  --role-name RoleForCertManager \<br />  --assume-role-policy-document file://trustpolicy.json</pre> | AWS DevOps |
| Attach the policy to the role. | Enter the following command in AWS CLI to attach the IAM policy to the IAM role. Replace `AWS_ACCOUNT_ID` with the ID of your AWS account. <pre>aws iam attach-role-policy \<br />  --policy-arn arn:aws:iam::AWS_ACCOUNT_ID:policy/PolicyForCertManager \<br />  --role-name RoleForCertManager</pre> | AWS DevOps |

### Set up the NGINX Ingress Controller in Amazon EKS
<a name="set-up-the-nginx-ingress-controller-in-amazon-eks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the NGINX Ingress Controller. | Install the most recent version of `nginx-ingress` using Helm. You can modify the `nginx-ingress` configuration according to your requirements before deploying it. This pattern uses an annotated, internal-facing Network Load Balancer and that is available in the `5-Nginx-Ingress-Controller` directory. <br />Install the NGINX Ingress Controller by running the following Helm command from the `5-Nginx-Ingress-Controller` directory.<br />`helm install test-nginx nginx-stable/nginx-ingress  -f  5-Nginx-Ingress-Controller/values_internal_nlb.yaml` | AWS DevOps |
| Verify that the NGINX Ingress Controller is installed. | Enter the `helm list` command. The output should show that the NGINX Ingress Controller is installed. | AWS DevOps |
| Create a Route 53 A record. | The A record points to the Network Load Balancer created by NGINX Ingress Controller.1. Get the DNS name of the Network Load Balancer. For instructions, see [Getting the DNS name for an ELB load balancer](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html#resource-record-sets-elb-dns-name-procedure).<br />2. On the Amazon Route 53 console, choose **Hosted Zones**.<br />3. Select the public hosted zone that you want to create the record in, and then choose **Create record**.<br />4. Enter a name for the record. <br />5. In **Record type**, choose **A - Routes traffic to IPv4 and some AWS resources**.  <br />6. Enable **Alias**.<br />7. In **Route traffic to**, do the following:Choose **Alias to Network Load Balancer**.Choose the AWS Region in which the Network Load Balancer is deployed.Enter the DNS name of the Network Load Balancer.<br />8. Choose **Create records**. | AWS DevOps |

### Set up NGINX VirtualServer on Amazon EKS
<a name="set-up-nginx-virtualserver-on-amazon-eks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy NGINX VirtualServer. | The NGINX VirtualServer resource is a load balancing configuration that is an alternative to the ingress resource. The configuration to create the NGINX VirtualServer resource is available in the `nginx_virtualserver.yaml` file in the `6-Nginx-Virtual-Server` directory. Enter the following command in `kubectl` to create the NGINX VirtualServer resource.<br />`kubectl apply -f  nginx_virtualserver.yaml`Make sure that you update the application domain name, certificate secret, and application service name in the `nginx_virtualserver.yaml` file. | AWS DevOps |
| Verify that NGINX VirtualServer is created. | Enter the following command in `kubectl` to verify that the NGINX VirtualServer resource was successfully created.<br />`kubectl get virtualserver`Verify that the `Host` column matches your application’s domain name. | AWS DevOps |
| Deploy the NGINX web server with TLS enabled. | This pattern uses a NGINX web server with TLS enabled as the application for testing end-to-end encryption. The configuration files required to deploy the test application are available in the `demo-webserver` directory. <br />Enter the following command in `kubectl` to deploy the test application.<br />`kubectl apply -f nginx-tls-ap.yaml` | AWS DevOps |
| Verify that the test application resources are created. | Enter the following commands in `kubectl` to verify that the required resources are created for the test application:+ `kubectl get deployments`Validate the `Ready` column and `Available` column.<br />+ `kubectl get pods \| grep -i example-deploy` Pods should be in `running` state.<br />+ `kubectl get configmap` <br />+ `kubectl get svc`  | AWS DevOps |
| Validate the application. | 1. Enter the following command by replacing the `<application-domain-name>` with the Route53 DNS name that you created earlier.<br />`curl --verbose https://<application-domain-name>`<br />2. Verify that you can access the application. | AWS DevOps |

## Related resources
<a name="set-up-end-to-end-encryption-for-applications-on-amazon-eks-using-cert-manager-and-let-s-encrypt-resources"></a>

**AWS resources**
+ [Creating records by using the Amazon Route 53 console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) (Amazon Route 53 documentation)
+ [Using a Network Load Balancer with the NGINX ingress controller on Amazon EKS](https://aws.amazon.com/blogs/opensource/network-load-balancer-nginx-ingress-controller-eks/) (AWS blog post)

**Other resources**
+ [Route 53](https://cert-manager.io/docs/configuration/acme/dns01/route53/) (cert-manager documentation)
+ [Configuring DNS01 Challenge Provider](https://cert-manager.io/docs/configuration/acme/dns01/) (cert-manager documentation)
+ [Let’s encrypt DNS challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge) (Let’s Encrypt documentation)
