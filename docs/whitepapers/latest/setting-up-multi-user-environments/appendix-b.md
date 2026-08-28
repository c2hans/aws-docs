---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/appendix-b.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix B: Example IAM user policies
<a name="appendix-b"></a>

 This section provides example IAM user policies for a class that uses AWS services, including policies for the professor, teaching assistant, and students. These policies are useful for setting up the “Limited User Access to AWS Management Console” and “Separate AWS Account for Each User” scenarios described earlier in this whitepaper. For more information about policies, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html).

## Example policies for professor (administrator)
<a name="example-policies-for-professor-administrator"></a>
+  Full administrator access:

  ```
  {
    "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }]
  }
  ```
+  Billing access:

  ```
  {
    "Statement": [
    {
      "Effect": "Allow",
       "Action": [
        "aws-portal:ViewBilling"
      ],
      "Resource": "*"
    }]
  }
  ```
+  Usage access (Example Policies for Teaching Assistant):

  ```
  {
    "Statement": [
    {
      "Effect": "Allow",
      "Action": [
          "aws-portal:ViewUsage"
      ],
      "Resource": "*"
    }]
  }
  ```
+  Full administrator access but no access for billing or usage information:

  ```
  {
    "Statement":[{
      "Effect":"Allow",
      "Action":"*",
      "Resource":"*"
    },
    {
      "Effect":"Deny",
      "Action":"aws-portal:*", "Resource":"*"
    }]
  }
  ```

## Example Policies for Students
<a name="example-policies-for-students"></a>
+  Permission to create and describe Amazon EBS volumes:
+  Permission to create and modify Amazon EC2 instances:

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
                  "ec2:DescribeInstances",
                  "ec2:DescribeImages",
                  "ec2:DescribeInstanceTypes",
                  "ec2:DescribeKeyPairs",
                  "ec2:DescribeVpcs",
                  "ec2:DescribeSubnets",
                  "ec2:DescribeSecurityGroups",
                  "ec2:CreateSecurityGroup",
                  "ec2:AuthorizeSecurityGroupIngress",
                  "ec2:CreateKeyPair"
              ],
              "Resource": "*"
          },
          {
              "Effect": "Allow",
              "Action": "ec2:RunInstances",
              "Resource": "*"
          }
      ]
  }
  ```

------
+  Prevents modifying resource tags:

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
    {
      "Action": [
         "ec2:CreateTags",
          "ec2:DeleteTags"
      ],
      "Resource": [ "*"],
    "Effect": "Deny"
    }]
  }
  ```

------
+  For instances with a student tag, allows students to restart, stop, reboot, attach volumes, and detach volumes. If the professor or teaching assistant applies a student tag with the value being the IAM user name of specific students to specific instances, then those students can stop, reboot, attach volumes to, and detach volumes to those instances. They can also start instances that they stopped (that still have the student tag on them), but they can’t start new ones.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
