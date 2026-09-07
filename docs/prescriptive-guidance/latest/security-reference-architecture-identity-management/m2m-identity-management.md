---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/m2m-identity-management.html
---

# Machine-to-machine identity management
<a name="m2m-identity-management"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

Machine-to-machine (M2M) authentication enables services and applications that run on AWS to securely communicate with one another to access resources and data. Instead of using long-term static credentials, machine authentication systems issue temporary credentials or tokens to identify trusted machines. They allow precise control over which machines can access specific parts of the environment without human intervention. Well-designed machine authentication helps improve your security posture by limiting broad credential exposure, enabling dynamic revocation of permissions, and simplifying credential rotation. Typical methods for machine authentication include EC2 instance profiles, the Amazon Cognito client credentials grant, mutually authenticated TLS (mTLS) connections, and IAM Roles Anywhere. This section provides guidance on implementing secure and scalable M2M authentication flows on AWS.

## EC2 instance profiles
<a name="m2m-instance-profiles"></a>

For scenarios where you have an application or service running on Amazon Elastic Compute Cloud (Amazon EC2) that needs to call AWS APIs, consider using EC2 instance profiles. Instance profiles allow applications that run on EC2 instances to securely access other AWS services without requiring static, long-lived IAM access keys. Instead, you should assign an IAM role to your instance to provide the required permissions through the instance profile. The EC2 instance can then automatically obtain temporary security credentials from the instance profile to access other AWS services.

The following diagram illustrates this scenario.

![Using EC2 instance profiles for machine-to-machine identity management.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/bbc5f256-2826-4039-86dc-9d7a1c9b4a24.png)

1. An application on the EC2 instance that needs to call an AWS API retrieves the security credentials provided by the role from the instance metadata item `iam/security-credentials/<role-name>`.

1. The application receives the `AccessKeyId`, `SecretAccessKey`, and a secret token that can be used to sign AWS API requests.

1. The application calls an AWS API. If the role permits the API action, the request is successful.

To learn more about using temporary credentials with AWS resources, see [Use temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM documentation.

**Benefits:**
+ **Improved security**. This method avoids the distribution of long-term credentials to EC2 instances. Credentials are provided temporarily through the instance profile.
+ **Easy integration**. Applications that run on the instance can automatically obtain credentials without any additional coding or configuration. The AWS SDKs automatically use the instance profile credentials.
+ **Dynamic permissions**. You can change the permissions that are available to the instance by updating the IAM role that's assigned to the instance profile. New credentials that reflect the updated permissions are automatically obtained.
+ **Rotation**. AWS automatically rotates the temporary credentials to reduce the risk from compromised credentials.
+ **Revocation**. You can revoke the credentials immediately by removing the role assignment from the instance profile.

**Design considerations**
+ An EC2 instance can have only one attached instance profile.
+ Use least privilege IAM roles. Assign only the permissions that your application requires to the IAM role for the instance profile. Start with minimum permissions and add more permissions later if needed.
+ Use IAM conditions in the role policy to restrict permissions based on tags, IP address ranges, time of day, and so on. This limits the services and resources the application can access.
+ Consider how many instance profiles you require. All applications that run on an EC2 instance share the same profile and have the same AWS permissions. You can apply the same instance profile to multiple EC2 instances, so you can reduce administrative overhead by reusing instance profiles where appropriate.
+ Monitor activity. Use tools such as AWS CloudTrail to monitor API calls that use the instance profile credentials. Watch for unusual activity that could indicate compromised credentials.
+ Delete unneeded credentials. Remove role assignments from unused instance profiles to prevent the use of credentials. You can use IAM access advisor to identify unused roles.
+ Use the PassRole permission to restrict which role a user can pass to an EC2 instance when they launch the instance. This prevents the user from running applications that have more permissions than the user has been granted.
+ If your architecture spans multiple AWS accounts, consider how EC2 instances in one account might need to access resources in another account. Use cross-account roles appropriately to ensure secure access without having to embed long-term AWS security credentials.
+ To manage instance profiles at scale, you can use one of these options:
  + Use AWS Systems Manager Automation runbooks to automate the association of instance profiles to EC2 instances. This can be done at launch time, or after an instance is running.
  + Use AWS CloudFormation to apply instance profiles to EC2 instances programmatically at creation time, instead of configuring them through the AWS console.
+ It's good practice to use VPC endpoints to privately connect to supported AWS services such as Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB from applications that run on EC2 instances.

## Amazon Cognito client credentials grant
<a name="m2m-cognito"></a>

[Amazon Cognito](https://aws.amazon.com/cognito/) is a managed customer identity and access management service. Amazon Cognito provides OAuth-compliant authentication flows, including the ability to authenticate machines or applications instead of users through the client credentials grant type. This grant allows an application to directly retrieve temporary AWS credentials to access AWS services. Amazon Cognito client credentials are a secure way to provide AWS permissions to applications without human user interaction. Applications present their client ID and client secret to the Amazon Cognito token endpoint. In return, they receive an access token, which they can use to authenticate subsequent requests to various resources and services. The scope of this access is dictated by the permissions that are associated with the client ID. The application that receives the request must validate the token by checking its signature, expiration timestamp, and audience. After these checks, the application verifies that the requested action is allowed by validating the claims in the token.

The following diagram illustrates this method.

![Using Amazon Cognito client credentials for machine-to-machine identity management.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/3e2fab9c-a4f0-41e6-a33c-a7233d111178.png)

1. The application (App Client) that wants to request resources from a server (Resource Server) requests a token from Amazon Cognito.

1. Amazon Cognito user pools return an access token.

1. App Client sends a request to Resource Server and includes the access token.

1. Resource Server validates the token with Amazon Cognito.

1. If validation is successful and the requested action is allowed, Resource Server responds with the requested resource.

**Benefits:**
+ **Machine authentication**. This method doesn't require user context or logins. The application authenticates directly with tokens.
+ **Short-term credentials**. Applications can obtain an access token first from Amazon Cognito and then use the time-bound access token to access data from the resource server.
+ **OAuth2 support**. This method reduces inconsistencies and helps with application development because it follows the established OAuth2 standard.
+ **Enhanced security**. Using the client credentials grant provides enhanced security, because the client ID and client secret aren't transferred to the resource server, unlike an API key authorization mechanism. The client ID and secret are shared and used only when making calls to Amazon Cognito to get time-bound access tokens.
+ **Fine-grained access control through scopes**. The application can define and request scopes and additional claims to limit access to only specific resources.
+ **Audit trail**. You can use the information collected by CloudTrail to determine the request that was made to Amazon Cognito, the IP address from which the request was made, who made the request, when it was made, and additional details.

**Design considerations:**
+ Carefully define and constrain the scope of access for each client ID to the minimum required. Tight scopes help reduce potential vulnerabilities and ensure that services have access only to necessary resources.
+ Protect client IDs and secrets by using secure storage services such as AWS Secrets Manager to store credentials. Do not check credentials into source code.
+ Monitor and audit token requests and usage with tools such as CloudTrail and CloudWatch. Watch for unexpected activity patterns that could indicate issues.
+ Automate the rotation of client secrets on a regular schedule. With each rotation, create a new application client, delete the old client, and update the client ID and secret. Facilitate these rotations without disrupting service communications.
+ Enforce rate limits on token endpoint requests to help prevent abuse and denial of service (DoS) attacks.
+ Have a strategy ready for [revoking tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html) in the event of a security breach. Although tokens are short-lived, compromised tokens should be invalidated immediately.
+ Use AWS CloudFormation to programmatically create Amazon Cognito user pools and the application clients that represent the machines that need to authenticate to other services.
+ Where appropriate, [cache tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-caching-tokens.html) to provide performance efficiency and cost optimization.
+ Ensure that the expiration of access tokens aligns with your organization's security posture.
+ If you use a custom resource server, always verify the access token to ensure that the signature is valid, the token hasn't expired, and the correct scopes are present. Verify any additional claims as needed.
+ To manage client credentials at scale, you can use one of these options:
  + Centralize the management of all client credentials in a single centralized Amazon Cognito instance. This can reduce the management overhead of multiple Amazon Cognito instances, and can make configuration and auditing simpler. However, make sure to plan for scale and consider the Amazon Cognito[ service quotas](https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html).
  + Federate the responsibility for client credentials to workload accounts and allow multiple Amazon Cognito instances. This option promotes flexibility but can increase overhead and overall complexity compared with the centralized option.

## mTLS authentication
<a name="m2m-mtls"></a>

Mutual TLS (mTLS) authentication is a mechanism that allows both the client and the server to authenticate to each other before they communicate by using certificates with TLS. Common use cases for mTLS include industries with high regulations, Internet of Things (IoT) applications, and business-to-business (B2B) applications. Amazon API Gateway currently supports mTLS in addition to its existing authorization options. You can enable mTLS on custom domains to authenticate against Regional REST and HTTP APIs. Requests can be authorized by using Bearer, JSON Web Tokens (JWTs), or sign requests with IAM-based authorization.

The following diagram shows the mTLS authentication flow for an application that's running on an EC2 instance and an API that's set up on API Gateway.

![mTLS authentication for an application that's running on an EC2 instance.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/7476db30-4b98-493f-a41e-6debc8bb5226.png)

1. API Gateway requests a publicly trusted certificate directly from AWS Certificate Manager (ACM).

1. ACM generates the certificate from its certificate authority (CA).

1. The client that calls the API presents a certificate with the API request.

1. API Gateway checks the Amazon S3 trust store bucket that you have created. This bucket contains the X.509 certificates that you trust to access your API. For API Gateway to proceed with the request, the certificate's issuer and the complete chain of trust up to the root CA certificate must be in your trust store.

1. If the clients' certificate is trusted, API Gateway approves the request and calls the method.

1. The associated API action (in this case, an AWS Lambda function) processes the request and returns a response that is sent to the requestor.

**Benefits**
+ **M2M authentication**. Services authenticate one another directly instead of using shared secrets or tokens. This removes the need to store and manage static credentials.
+ **Tamper protection**. TLS encryption protects data in transit between services. Communications cannot be read or altered by third parties.
+ **Easy integration**. mTLS support is built into major programming languages and frameworks. Services can enable mTLS with minimal code changes.
+ **Granular permissions**. Services trust only specific certificates, which allows fine-grained control over permitted callers.
+ **Revocation**. Compromised certificates can be revoked immediately so they are no longer trusted, preventing further access.

**Design considerations:**
+ When you use API Gateway:
  + By default, clients can call your API by using the `execute-api` endpoint that API Gateway generates for your API. To ensure that clients can access your API only by using a custom domain name with mTLS, disable this default  endpoint. To learn more, see [Disable the default endpoint for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-disable-default-endpoint.html) in the API Gateway documentation.
  + API Gateway doesn't verify whether certificates have been revoked.
  + To configure mTLS for a REST API, you must use a Regional custom domain name for your API, with a minimum TLS version of 1.2. mTLS isn't supported for private APIs.
+ You can issue certificates for API Gateway from your own CA or import them from AWS Private Certificate Authority.
+ Create processes to securely issue, distribute, renew, and revoke service certificates. Automate issuance and renewal where possible. If one side of your M2M communication is an API gateway, you can integrate with AWS Private CA.
+ Safeguard access to the private CA. Compromising the CA compromises trust in all certificates it issued.
+ Store private keys securely and separately from certificates. Rotate keys periodically to limit impact if compromised.
+ Revoke certificates immediately when they're no longer needed or if they're compromised. Distribute certificate revocation lists to services.
+ Where possible, issue certificates that are intended for only specific purposes or resources to limit their utility if they're compromised.
+ Have contingency plans for certificate expirations and outages of the CA or certificate revocation list (CRL) infrastructure.
+ Monitor your system for certificate failures and outages. Watch for spikes in failures that could indicate issues.
+ If you are using ACM with AWS Private CA, you can use AWS CloudFormation to programmatically request public and private certificates.
+ If you are using ACM, use AWS Resource Access Manager (AWS RAM) to share the certificate from a security account to the workload account.

## IAM Roles Anywhere
<a name="mtm-iam-roles-anywhere"></a>

We recommend that you use [IAM Roles Anywhere](https://aws.amazon.com/iam/roles-anywhere/) for M2M identity management when machines or systems need to connect to AWS services but do not support IAM roles. IAM Roles Anywhere is an extension of IAM that uses public key infrastructure (PKI) to grant access to workloads by using temporary security credentials. You can use X.509 certificates, which can be issued either through a CA or by [AWS Private CA](https://aws.amazon.com/private-ca/), to establish a trust anchor between the CA and IAM Roles Anywhere. As with IAM roles, the workload can access AWS services based on its permission policy, which is attached to the role.

The following diagram shows how you can use IAM Roles Anywhere to connect AWS with external resources.

![Using IAM Roles Anywhere for machine-to-machine identity management.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/b6cb04c1-e955-49d5-9d09-84c3317d4fda.png)

1. You create a trust anchor to establish trust between your AWS account and the CA that issues certificates to your on-premises workloads. The certificates are issued by a CA that you register as a [trust anchor](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user) (root of trust) in IAM Roles Anywhere. The CA can be part of your existing public key infrastructure (PKI) system, or it can be a CA that you created with AWS Private CA and manage with ACM. In this example, we are using ACM.

1. Your application makes an authentication request to IAM Roles Anywhere, and sends its public key (encoded in a certificate) and a signature signed by the corresponding private key. Your application also specifies the role to assume in the request.

1. When IAM Roles Anywhere receives the request, it first validates the signature with the public key, and then validates that the certificate was issued by a trust anchor. After both validations succeed, your application is authenticated and IAM Roles Anywhere creates a new role session for the role specified in the request by calling [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html).

1. You use the [credential helper tool ](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/credential-helper.html)that IAM Roles Anywhere provides to manage the process of creating a signature with the certificate and to call the endpoint to obtain session credentials. The tool returns the credentials to the calling process in a standard JSON format.

1. By using this bridged trust model between IAM and PKI, on-premises workloads use these temporary credentials (access key, secret key, and session token) to assume the IAM role to interact with AWS resources without needing long-term credentials. You can also configure these credentials by using the AWS CLI or AWS SDKs.

**Benefits:**
+ **No permanent credentials**. Applications don't need long-term AWS access keys with broad permissions.
+ **Fine-grained access**. Policies determine which IAM role can be assumed for a specific entity.
+ **Context-aware roles**. The role can be customized based on the details of the authenticated entity.
+ **Revocation**. Revoking trust permissions immediately blocks an entity from assuming a role.

**Design considerations: **
+ Servers must be able to support certificate-based authentication.
+ It's good practice to lock down the trust policy to use `aws:SourceArn` or `aws:SourceAccount` for the account where the trust anchor has been configured.
+ Principal tags are carried forward from the certificate details. These include the common name (CN), the subject alternative name (SAN), the subject, and the issuer.
+ If you are using ACM, use AWS RAM to share the certificate from a security account to the workload account.
+ Use operating system (OS) file system permissions to restrict read access to the owning user.
+ Never check keys into source control. Store them separately from source code to reduce the risk of accidentally including them in a change set. If possible, consider using a secure storage mechanism.
+ Make sure that you have a process to rotate and revoke certificates.

## Amazon VPC Lattice
<a name="mtm-vpc-lattice"></a>

For scenarios where you would like to connect multiple applications or services that run across the same or different compute platforms―such as EC2 instances, Lambda functions, or even Kubernetes pods―without increasing networking complexity, consider [Amazon VPC Lattice](https://aws.amazon.com/vpc/lattice/). This application networking service connects, monitors, and secures service-to-service communications. A [service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html), often called a *microservice*, is an independently deployable unit of software that delivers a specific task. VPC Lattice automatically manages network connectivity and application-layer routing between services across VPCs and AWS accounts without requiring you to manage the underlying network connectivity, frontend load balancers, or sidecar proxies.

The following diagram shows an example of a VPC Lattice service network, which comprises one or more VPC Lattice services. The services are part of a service directory, which is a list of all VPC Lattice services you create locally within an AWS account together with any VPC Lattice services that are shared with your account by using AWS RAM.

![VPC Lattice service network with multiple services.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/0d01567b-4cb7-432f-82c3-6781569492d0.png)

1. A service network is a logical boundary for a collection of services. Services that are associated with the network can be authorized for discovery, connectivity, accessibility, and observability. To make requests to services in the network, the client must be in a VPC that is associated with the service network.

1. A service represents an independently deployable unit of software that delivers a specific task or function. Each service has a listener that uses rules to target to one or several target groups. Targets can be EC2 instances, IP addresses, Lambda functions, Application Load Balancers, or Kubernetes pods.

1. Associating a service with a service network enables clients to make requests to the service, but only if the VPC where the client is located is also associated with the service network, and the policies allow it.

1. Associating a VPC with the service network enables all the targets within that VPC to be clients and communicate with other services in the service network. A security group can be attached to this association to control the network access from the VPC, and service network or service policies can be used to apply fine-grained access controls.

Authentication and authorization are enforced by using [auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html), which are IAM policy documents that are attached to service networks (for coarse-grained controls) or individual services (for fine-grained controls) to control principal access to services.

After services are associated with the service network, they can begin interacting without any networking changes required to enable the communications. This helps reduce the overhead of complex networking.

**Benefits:**
+ **Improved security**. Creates an improved and more consistent security posture with reliable authentication and context-specific authorization by using IAM.
+ **Simplified connectivity**. Using VPC Lattice to discover and securely connect services and resources across VPCs and accounts helps simplify and automate service and resource connectivity.
+ **Connecting compute platforms**. You can connect platforms such as EC2 instances, Lambda functions, and Amazon Elastic Kubernetes Service (Amazon EKS services to a single service network.
+ **Scalability**. You can scale compute and network resources automatically to support high-bandwidth HTTP, HTTPS, gRPC, and TCP workloads.
+ **Connecting TCP resources**. You can connect to TCP resources such as Amazon Relational Database Service (Amazon RDS) databases, domain names, and IP addresses across multiple VPCs and accounts.

**Design considerations:**
+ Plan your service topology carefully, evaluate which VPCs need to be connected to the network, and identify areas where dedicated service networks are required for isolation. Design traffic routing rules and weights, plan health check configurations, and consider circuit breakers.
+ Consider [external connectivity patterns](https://aws.amazon.com/solutions/guidance/external-connectivity-to-amazon-vpc-lattice/) such as hybrid and cross-Region access.
+ Design authentication and authorization policies by using IAM constructs at the network and endpoint level based on your security requirements.
+ For operational aspects such as deployment automation and procedures for introducing changes to networks and services, consider how services will be discovered by clients.
+ To optimize costs, evaluate pricing based on the number of services and networks. Consider costs for Availability Zone traffic, and optimize the number of service endpoints.
+ Consider [service quotas](https://docs.aws.amazon.com/vpc-lattice/latest/ug/quotas.html).
