---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/aws-waf-restrict-access-geolocation.html
---

# Restrict access based on IP address or geolocation by using AWS WAF
<a name="aws-waf-restrict-access-geolocation"></a>

*Louis Hourcade, Amazon Web Services*

## Summary
<a name="aws-waf-restrict-access-geolocation-summary"></a>

[AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) is a web application firewall that helps protect web applications and APIs against common web exploits and bots that can affect availability, compromise security, or consume excessive resources. [Web access control lists (web ACLs)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html) in AWS WAF give you control over how traffic reaches your applications. In a web ACL, you add rules or rule groups that are designed to permit legitimate traffic, control bot traffic, and block common attack patterns. For more information, see [How AWS WAF works](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html).

You can associate the following types of rules to your AWS WAF web ACLs:
+ [Managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups.html) – AWS Managed Rules teams and AWS Marketplace sellers offer preconfigured sets of rules. Some managed rule groups are designed to help protect specific types of web applications. Others offer broad protection against known threats or common vulnerabilities.
+ [Custom rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html) and [custom rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-user-created-rule-groups.html) – You can also create rules and rule groups that customize access to your web applications and APIs. For example, you can restrict traffic based on a specific list of IP addresses or on a list of countries.

By using this pattern and the associated code repository, you can use the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) to deploy AWS WAF web ACLs with custom rules. These rules restrict access to web application resources based on the end user's IP address or geolocation. You can also optionally attach several managed rule groups.

## Prerequisites and limitations
<a name="aws-waf-restrict-access-geolocation-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ [Permissions](https://docs.aws.amazon.com/waf/latest/developerguide/security-iam.html) to deploy AWS WAF resources
+ AWS CDK, [installed and configured](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) in your account
+ Git, [installed](https://github.com/git-guides/install-git)

**Limitations**
+ You can use this pattern only in AWS Regions where AWS WAF is available. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

## Tools
<a name="aws-waf-restrict-access-geolocation-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) is a web application firewall that helps you monitor HTTP and HTTPS requests that are forwarded to your protected web application resources.

**Code repository**

The code for this pattern is available in the GitHub [IP and geolocation restriction with AWS WAF](https://github.com/aws-samples/ip-and-geolocation-restriction-with-waf-cdk) repository. The code deploys two AWS WAF web ACLs. The first is a regional web ACL that is intended for [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) resources. The second is global web ACL for [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) resources. Both web ACLs contain the following custom rules:
+ `IPMatch` blocks requests from non-allowed IP addresses.
+ `GeoMatch` blocks requests from non-allowed countries.

During deployment, you can optionally attach all of the following managed rule groups to your web ACLs:
+ [Core rule set (CRS)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-crs) – This rule group contains rules that are generally applicable to web applications. It helps protect against exploitation of a wide range of vulnerabilities, including some of the high risk and commonly occurring vulnerabilities described in OWASP publications, such as [OWASP Top 10](https://owasp.org/www-project-top-ten/).
+ [Admin protection](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-admin) – This rule group contains rules that help you block external access to exposed administrative pages.
+ [Known bad inputs](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-known-bad-inputs) – This rule group helps block request patterns that are known to be invalid and are associated with the exploitation or discovery of vulnerabilities.
+ [Amazon IP reputation list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html#aws-managed-rule-groups-ip-rep-amazon) – This rule group contains rules that are based on Amazon internal threat intelligence. It helps you block IP addresses that are typically associated with bots or other threats.
+ [Linux operating system managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html#aws-managed-rule-groups-use-case-linux-os) – This rule group helps block request patterns that are associated with the exploitation of Linux vulnerabilities, including Linux-specific Local File Inclusion (LFI) attacks.
+ [SQL database managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html#aws-managed-rule-groups-use-case-sql-db) – This rule group helps block request patterns that are associated with the exploitation of SQL databases, such as SQL injection attacks.

## Epics
<a name="aws-waf-restrict-access-geolocation-epics"></a>

### Configure the AWS WAF web ACLs
<a name="configure-the-waf-web-acls"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Enter the following command to clone the [IP and geolocation restriction with AWS WAF](https://github.com/aws-samples/ip-and-geolocation-restriction-with-waf-cdk) repository to your local workstation:<pre>git clone https://github.com/aws-samples/ip-and-geolocation-restriction-with-waf-cdk.git</pre> | Git |
| Configure the rules. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/aws-waf-restrict-access-geolocation.html) | General AWS, Python |

### Bootstrap and deploy the code
<a name="bootstrap-and-deploy-the-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Bootstrap your AWS environment. | If not already done, you need to [bootstrap](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping-env.html) your AWS environment before you can deploy the AWS CDK application.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/aws-waf-restrict-access-geolocation.html) | General AWS |
| Deploy the AWS CDK application. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/aws-waf-restrict-access-geolocation.html) | General AWS |

### Validate the deployment
<a name="validate-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm that the web ACLs successfully deployed. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/aws-waf-restrict-access-geolocation.html) | General AWS |
| (Optional) Associate the web ACLs to your resources. | Associate the AWS WAF web ACLs with your AWS resources, such as an Application Load Balancer, API Gateway, or CloudFront distribution. For instructions, see [Associating or disassociating a web ACL with an ](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html)AWS[ resource](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html). For an example, see [class CfnWebACLAssociation (construct)](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_wafv2.CfnWebACLAssociation.html) in the AWS CDK documentation. | General AWS |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the stacks. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/aws-waf-restrict-access-geolocation.html) | General AWS |

## Related resources
<a name="aws-waf-restrict-access-geolocation-resources"></a>
+ [API Reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html) (AWS CDK documentation)
+ [aws-cdk-lib.aws\_wafv2 module](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_wafv2-readme.html) (AWS CDK documentation)
+ [Working with web ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-working-with.html) (AWS WAF documentation)
+ [Managing your own rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-user-created-rule-groups.html) (AWS WAF documentation)
+ [Rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html) (AWS WAF documentation)
