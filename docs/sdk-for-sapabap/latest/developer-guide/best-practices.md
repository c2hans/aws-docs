---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/best-practices.html
---

# Best practices for IAM Security
<a name="best-practices"></a>

The IAM administrator will be responsible for the following three key areas.
+ Ensuring that the SAP system can authenticate itself with Amazon EC2 metadata or Secret Key credentials.
+ Ensuring that the SAP system has the permissions it needs to elevate itself with `sts:assumeRole`.
+ For each logical IAM role, creating an IAM role for SAP users with the permissions required to perform the business functions (for example, the necessary permissions for Amazon S3, DynamoDB, or other services). These are the roles that SAP users will assume.

For more information, see the [Security](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/security.html) chapter in the SAP Lens: AWS Well-Architected Framework.

**Topics**
+ [Best practice for Amazon EC2 instance profile](#best-practice-instance-profile)
+ [IAM roles for SAP users](#iam-roles-sap-users)
+ [Source Profile Security Considerations](#source-profile-security)

## Best practice for Amazon EC2 instance profile
<a name="best-practice-instance-profile"></a>

The Amazon EC2 instance on which your SAP system runs has a set of authorizations based on its instance profile. Generally, the instance profile only needs to have permissions to call `sts:assumeRole`, to allow the SAP system to assume business-specific IAM roles as needed. This elevation to other roles ensures that an ABAP program can assume a role that gives the user the least privilege needed to do their job. For example, an instance profile might contain the following statement.

------
#### [ JSON ]

****

```
{
 "Version":"2012-10-17",
 "Statement": [
   {
     "Sid": "VisualEditor0",
     "Effect": "Allow",
     "Action": "sts:AssumeRole",
     "Resource":[
        "arn:aws:iam::012345678912:role/finance-cfo",
        "arn:aws:iam::012345678912:role/finance-auditor",
        "arn:aws:iam::012345678912:role/finance-reporting"
      ]
   }
 ]
}
```

------

This preceding example allows the SAP system to assume the IAM roles for the CFO, AUDITOR, or REPORTING user. AWS SDK will choose the correct IAM role for the user based on the user’s PFCG role in SAP.

Amazon EC2 instance profile can also be used for other functions.
+ [AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-sap-hana.html)
+ [SAP on AWS High Availability with Overlay IP Address Routing](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-ha-overlay-ip.html)

These solutions may also require `sts:assumeRole` permissions to roles specific to backup or failover or they may require permissions to be assigned directly to the instance profile.

## IAM roles for SAP users
<a name="iam-roles-sap-users"></a>

The ABAP program needs permissions to perform the user’s job: read a DynamoDB table, invoke Amazon Textract on a PDF object in Amazon S3, run an AWS Lambda function. The same security model is used in all AWS SDKs. You can use an existing IAM role that was used for another AWS SDK.

The SAP business analyst will ask the IAM administrator for the arn:aws: of an IAM role for each logical role needed. For example, in a financial scenario, the business analyst may define the following logical IAM roles.
+  `CFO`
+  `AUDITOR`
+  `REPORTING`

The IAM administrator will define IAM roles for each logical IAM role.

 `CFO`
+  `arn:aws:iam::{{0123456789}}:role/finance-cfo`
+ read and write permissions to an Amazon S3 bucket
+ read and write permissions to a DynamoDB database

 `AUDITOR`
+  `arn:aws:iam::{{0123456789}}:role/finance-auditor`
+ read permissions to an Amazon S3 bucket
+  read permissions to a DynamoDB database

 `REPORTING`
+  `arn:aws:iam::{{0123456789}}:role/finance-reporting`
+ read permissions to a DynamoDB database
+ no permission for the Amazon S3 bucket

The business analyst will enter the IAM roles into a mapping table to map the logical IAM roles with the physical IAM roles.

IAM roles for SAP users need to allow the `sts:assumeRole` action for trusted principals. The trusted principals can vary based on how the SAP system is authenticated on AWS. For more details, see [Specifying a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying).

The following are some examples of the most common SAP scenarios.
+ **SAP system running on Amazon EC2 with an instance profile assigned** – here, an Amazon EC2 instance profile is attached to an IAM role.

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:AssumeRole"
              ],
              "Principal": {
                  "AWS": "arn:aws:iam::{{123456789012}}:role/{{SapInstanceProfile}}"
              }
          }
      ]
  }
  ```

------
+ **SAP systems running on Amazon EC2 without an instance profile** – here, Amazon EC2 assumes roles for SAP users.

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:AssumeRole"
              ],
              "Principal": {
                  "Service": [ "ec2.amazonaws.com" ]
              }
          }
      ]
  }
  ```

------
+ **SAP systems running on-premises** – SAP systems that run on-premises can only authenticate using the Secret Access Key. For more information, see [SAP system authentication on AWS](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/system-authentication.html).

  Here, any IAM role assumed by an SAP user must have a trust relationship that trusts the SAP user.

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:AssumeRole"
              ],
              "Principal": {
                  "AWS": "arn:aws:iam::{{123456789012}}:user/{{SAP_SYSTEM_S4}}H"
              }
          }
      ]
  }
  ```

------

## Source Profile Security Considerations
<a name="source-profile-security"></a>

When using source profile:

### IAM Role Management
<a name="iam-role-management"></a>

**Critical**: IAM roles in source profile chains must be strictly managed to prevent unauthorized access and privilege escalation:
+ **Apply least privilege principle** - Grant only the minimum permissions required for each role's specific purpose
+ **Regularly audit role permissions** - Review and update role policies quarterly or when requirements change
+ **Monitor role usage** - Use to track AssumeRole API calls and identify unusual patterns
+ **Limit trust relationships** - Restrict which principals can assume each role to only those that absolutely need access
+ **Use conditions in trust policies** - Add conditions like source IP, MFA requirements, or time-based restrictions where appropriate
+ **Document role purposes** - Maintain clear documentation of each role's intended use case and required permissions

### Authorization and Access Control
<a name="authorization-access-control"></a>
+ Ensure all intermediate profiles in the chain have appropriate trust policies configured
+ Users must have `/AWS1/SESS` authorization for ALL profiles in the chain, including intermediate profiles
+ Each IAM role must explicitly trust the previous role in the chain

### Technical Safeguards
<a name="technical-safeguards"></a>
+ The SDK enforces a maximum chain depth of 5 profiles to prevent excessive STS API calls
+ Circular references are automatically detected and prevented
+ Base profile authentication method is validated to ensure it uses a standard method (INST, SSF, or RLA)

For more information about configuring source profile, see [Using Source Profile for Cross-Account Access](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/source-profile.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
