---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about deploying and using Cloud Migration Factory.

## How do I know if this solution is suitable for my project?
<a name="q1"></a>

Cloud Migration Factory is suitable for customers who have more than 100 servers that they want to rehost on AWS. Those servers must also be within the list of [supported operating systems](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html) for AWS Transform MGN.

## How much does it cost to run Cloud Migration Factory?
<a name="q2"></a>

Cloud Migration Factory is a serverless solution that uses AWS services such as Amazon Simple Storage Service (Amazon S3), Amazon CloudFront, Amazon DynamoDB, and AWS Lambda. Your cost depends on your usage.

## How can I deploy or get support for Cloud Migration Factory?
<a name="q3"></a>

To deploy Cloud Migration Factory, see the [AWS Cloud Migration Factory Solution](https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/) on the AWS Solutions website. The source code is available in a [GitHub repository](https://github.com/awslabs/aws-cloudendure-migration-factory-solution). If you have any questions, email AWS Professional Services at *migration-factory-support@amazon.com*. We will be happy to help you.

## After I deploy Cloud Migration Factory, can AWS help me migrate my servers using this solution?
<a name="q4"></a>

Yes, the AWS Professional Services team can help you. Please email us at *migration-factory-support@amazon.com* and tell us about your use cases. This process includes:
+ An initial conversation to discuss your business case
+ A one-hour Cloud Migration Factory introduction and demo session with your team
+ Migration immersion day with Cloud Migration Factory, including a half-day lab session followed by Q&A
+ Discussion of resources you might need from AWS Professional Services

## What permissions do I need to deploy the migration factory solution?
<a name="q5"></a>

Ideally, you will need to use AWS administrator credentials to deploy the stack. If not, we can provide AWS Identity and Access Management (IAM) policies for you to attach to the user who will deploy the factory.

## What permissions do I need to run the automation scripts?
<a name="q6"></a>

For Windows, you need a domain user with local administrator credentials to access all Windows servers. For Linux, you need a sudo user with NOPASSWD enabled.

## What firewall rules do I need to create for the migration execution server?
<a name="q7"></a>

The migration execution server needs to access source servers and external APIs (AWS Transform MGN, Cloud Migration Factory, and AWS APIs). The server needs access to the internet to access these APIs. You can use a proxy server, but if you do, the proxy server can't use authentication. The server needs SSH access to the source Linux server on TCP port 22, or Windows Remote Management (WinRM) access to the source Windows server on TCP port 5985.

## Can I customize the Cloud Migration Factory schema to capture additional attributes?
<a name="q8"></a>

Yes, you can modify or extend the schema to capture additional server or application attributes.

## Why doesn't the CSV file include all Amazon EC2 launch template attributes?
<a name="q9"></a>

Cloud Migration Factory hides uncommon attributes, such as IAM role and public IP. However, you can add these attributes to the CSV file and import them to update the Amazon Elastic Compute Cloud (Amazon EC2) launch templates.

## Can I bulk-update the Amazon EC2 launch templates for all my servers?
<a name="q10"></a>

Yes, you can set hardcoded values for any Amazon EC2 launch template attribute. For example, Cloud Migration Factory sets a private IP for all servers and sets the disk to use gp2 volumes by default, but you can update these attributes.

## Does Cloud Migration Factory support SAML federation?
<a name="q11"></a>

Security Assertion Markup Language (SAML) federation isn't currently supported.

## What should I do if using Launch Server or Check Status in Cloud Migration Factory displays an "Unexpected timeout" error?
<a name="q12"></a>

If you receive a timeout error, your Cloud Migration Factory login token might have expired. Refresh the web page to get a new token.
