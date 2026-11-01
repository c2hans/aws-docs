---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_organizations_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Organizations examples using AWS CLI
<a name="cli_2_organizations_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Organizations.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `accept-handshake`
<a name="organizations_AcceptHandshake_cli_2_topic"></a>

The following code example shows how to use `accept-handshake`.

**AWS CLI**
**To accept a handshake from another account**
The following `accept-handshake` example accepts a handshake on behalf of Juan's account and thus agrees to the invitation. Bill, the owner of an organization, has previously invited Juan's account to join his organization.

```
aws organizations accept-handshake \
    --handshake-id {{h-examplehandshakeid111}}
```
Output:

```
{
    "Handshake": {
        "Action": "INVITE",
        "Arn": "arn:aws:organizations::123456789012:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
        "RequestedTimestamp": 1481656459.257,
        "ExpirationTimestamp": 1482952459.257,
        "Id": "h-examplehandshakeid111",
        "Parties": [
            {
                "Id": "o-exampleorgid",
                "Type": "ORGANIZATION"
            },
            {
                "Id": "juan@example.com",
                "Type": "EMAIL"
            }
        ],
        "Resources": [
            {
                "Resources": [
                    {
                        "Type": "MASTER_EMAIL",
                        "Value": "bill@amazon.com"
                    },
                    {
                        "Type": "MASTER_NAME",
                        "Value": "Org Master Account"
                    },
                    {
                        "Type": "ORGANIZATION_FEATURE_SET",
                        "Value": "ALL"
                    }
                ],
                "Type": "ORGANIZATION",
                "Value": "o-exampleorgid"
            },
            {
                "Type": "EMAIL",
                "Value": "juan@example.com"
            }
        ],
        "State": "ACCEPTED"
    }
}
```
For more information, see [Accepting or declining account invitations with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_accept-decline-invite.html) in the *AWS Organizations User Guide*.
+  For API details, see [AcceptHandshake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/accept-handshake.html) in *AWS CLI Command Reference*.

### `attach-policy`
<a name="organizations_AttachPolicy_cli_2_topic"></a>

The following code example shows how to use `attach-policy`.

**AWS CLI**
**Example 1: To attach a policy to an OU**
The following `attach-policy` example attaches a service control policy (SCP) to an OU.

```
aws organizations attach-policy \
    --policy-id {{p-examplepolicyid111}} \
    --target-id {{ou-examplerootid111-exampleouid111}}
```
For more information, see [Attaching organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_attach.html) in the *AWS Organizations User Guide*.
This command produces no output.
**Example 2: To attach a policy to an account**
The following `attach-policy` example attaches a service control policy directly to an account.

```
aws organizations attach-policy \
    --policy-id {{p-examplepolicyid111}} \
    --target-id {{123456789222}}
```
This command produces no output.
For more information, see [Attaching organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_attach.html) in the *AWS Organizations User Guide*.
+  For API details, see [AttachPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/attach-policy.html) in *AWS CLI Command Reference*.

### `cancel-handshake`
<a name="organizations_CancelHandshake_cli_2_topic"></a>

The following code example shows how to use `cancel-handshake`.

**AWS CLI**
**To cancel a handshake sent from another account**
The following `cancel-handshake` example cancels a handshake that Bill previously sent to invite Susan's account to join his organization. He changes his mind and decides to cancel the invitation before Susan accepts it. The output shows that the handshake state is now `CANCELED`.

```
aws organizations cancel-handshake \
    --handshake-id {{h-examplehandshakeid111}}
```
Output:

```
{
    "Handshake": {
        "Id": "h-examplehandshakeid111",
        "State":"CANCELED",
        "Action": "INVITE",
        "Arn": "arn:aws:organizations::123456789012:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
        "Parties": [
            {
                "Id": "o-exampleorgid",
                "Type": "ORGANIZATION"
            },
            {
                "Id": "susan@example.com",
                "Type": "EMAIL"
            }
        ],
        "Resources": [
            {
                "Type": "ORGANIZATION",
                "Value": "o-exampleorgid",
                "Resources": [
                    {
                        "Type": "MASTER_EMAIL",
                        "Value": "bill@example.com"
                    },
                    {
                        "Type": "MASTER_NAME",
                        "Value": "Master Account"
                    },
                    {
                        "Type": "ORGANIZATION_FEATURE_SET",
                        "Value": "CONSOLIDATED_BILLING"
                    }
                ]
            },
            {
                "Type": "EMAIL",
                "Value": "anika@example.com"
            },
            {
                "Type": "NOTES",
                "Value": "This is a request for Susan's account to join Bob's organization."
            }
        ],
        "RequestedTimestamp": 1.47008383521E9,
        "ExpirationTimestamp": 1.47137983521E9
    }
}
```
For more information, see [Managing pending account invitations with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_manage-invites.html) in the *AWS Organizations User Guide*.
+  For API details, see [CancelHandshake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/cancel-handshake.html) in *AWS CLI Command Reference*.

### `create-account`
<a name="organizations_CreateAccount_cli_2_topic"></a>

The following code example shows how to use `create-account`.

**AWS CLI**
**To create a member account that is automatically part of the organization**
The following `create-account` example creates a member account in an organization. The member account is configured with the name Production Account and the email address of susan@example.com. Organizations automatically creates an IAM role using the default name of OrganizationAccountAccessRole because the roleName parameter is not specified. Also, the setting that allows IAM users or roles with sufficient permissions to access account billing data is set to the default value of ALLOW because the IamUserAccessToBilling parameter is not specified. Organizations automatically sends Susan a "Welcome to AWS" email. The output shows that the request status is `IN_PROGRESS`.

```
aws organizations create-account \
    --email {{susan@example.com}} \
    --account-name {{"Production Account"}}
```
Output:

```
{
    "CreateAccountStatus": {
        "State": "IN_PROGRESS",
        "Id": "car-examplecreateaccountrequestid111"
    }
}
```
You can later query the current status of the request by providing the Id response value to the describe-create-account-status command as the value for the create-account-request-id parameter.
For more information, see [Creating a member account in an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) in the *AWS Organizations User Guide*.
+  For API details, see [CreateAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-account.html) in *AWS CLI Command Reference*.

### `create-organization`
<a name="organizations_CreateOrganization_cli_2_topic"></a>

The following code example shows how to use `create-organization`.

**AWS CLI**
**Example 1: To create a new organization**
The following `create-organization` example creates an organization using credentials from Bill's account 111111111111. The account becomes the master account in the new organization. Because he does not specify a features set, the new organization defaults to all features enabled and service control policies are enabled on the root.

```
aws organizations create-organization
```
Output:

```
{
    "Organization": {
        "AvailablePolicyTypes": [
            {
                "Status": "ENABLED",
                "Type": "SERVICE_CONTROL_POLICY"
            }
        ],
        "MasterAccountId": "123456789012",
        "MasterAccountArn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789012",
        "MasterAccountEmail": "bill@example.com",
        "FeatureSet": "ALL",
        "Id": "o-exampleorgid",
        "Arn": "arn:aws:organizations::123456789012:organization/o-exampleorgid"
    }
}
```
For more information, see [Creating an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html) in the *AWS Organizations User Guide*.
**Example 2: To create a new organization with only consolidated billing features enabled**
The following `create-organization` example creates an organization that supports only the consolidated billing features.

```
aws organizations create-organization \
    --feature-set {{CONSOLIDATED_BILLING}}
```
Output:

```
{
    "Organization": {
        "Arn": "arn:aws:organizations::123456789012:organization/o-exampleorgid",
        "AvailablePolicyTypes": [],
        "Id": "o-exampleorgid",
        "MasterAccountArn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789012",
        "MasterAccountEmail": "bill@example.com",
        "MasterAccountId": "123456789012",
        "FeatureSet": "CONSOLIDATED_BILLING"
    }
}
```
For more information, see [Creating an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html) in the *AWS Organizations User Guide*.
+  For API details, see [CreateOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organization.html) in *AWS CLI Command Reference*.

### `create-organizational-unit`
<a name="organizations_CreateOrganizationalUnit_cli_2_topic"></a>

The following code example shows how to use `create-organizational-unit`.

**AWS CLI**
**To create an OU in a root or parent OU**
The following `create-organizational-unit` example creates an OU that is named AccountingOU.

```
aws organizations create-organizational-unit \
    --parent-id {{r-examplerootid111}} \
    --name {{AccountingOU}}
```
Output:

```
{
    "OrganizationalUnit": {
        "Id": "ou-examplerootid111-exampleouid111",
        "Arn": "arn:aws:organizations::123456789012:ou/o-exampleorgid/ou-examplerootid111-exampleouid111",
        "Name": "AccountingOU"
    }
}
```
For more information, see [Creating an organizational unit (OU) with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/create_ou.html) in the *AWS Organizations User Guide*.
+  For API details, see [CreateOrganizationalUnit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organizational-unit.html) in *AWS CLI Command Reference*.

### `create-policy`
<a name="organizations_CreatePolicy_cli_2_topic"></a>

The following code example shows how to use `create-policy`.

**AWS CLI**
**Example 1: To create a policy with a text source file for the JSON policy**
The following `create-policy` example creates a service control policy (SCP) named `AllowAllS3Actions`. The policy contents are taken from a file on the local computer called `policy.json`.

```
aws organizations create-policy \
    --content {{file://policy.json}} \
    --name {{AllowAllS3Actions}} \
    --type {{SERVICE_CONTROL_POLICY}} \
    --description {{"Allows delegation of all S3 actions"}}
```
Contents of `policy.json`:

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```
Output:

```
{
    "Policy": {
        "Content": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"s3:*\"],\"Resource\":[\"*\"]}]}",
        "PolicySummary": {
            "Arn": "arn:aws:organizations::o-exampleorgid:policy/service_control_policy/p-examplepolicyid111",
            "Description": "Allows delegation of all S3 actions",
            "Name": "AllowAllS3Actions",
            "Type": "SERVICE_CONTROL_POLICY"
        }
    }
}
```
For more information, see [Creating organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_create.html) in the *AWS Organizations User Guide*.
**Example 2: To create a policy with a JSON policy as a parameter**
The following `create-policy` example creates the same SCP, this time by embedding the policy contents as a JSON string in the parameter. The string must be escaped with backslashes before the double quotes to ensure that they are treated as literals in the parameter, which itself is surrounded by double quotes.

```
aws organizations create-policy \
    --content "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"s3:*\"],\"Resource\":[\"*\"]}]}" \
    --name {{AllowAllS3Actions}} \
    --type {{SERVICE_CONTROL_POLICY}} \
    --description {{"Allows delegation of all S3 actions"}}
```
Output:

```
{
    "Policy": {
        "Content": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":[\"s3:*\"],\"Resource\":[\"*\"]}]}",
        "PolicySummary": {
            "Arn": "arn:aws:organizations::o-exampleorgid:policy/service_control_policy/p-examplepolicyid111",
            "Description": "Allows delegation of all S3 actions",
            "Name": "AllowAllS3Actions",
            "Type": "SERVICE_CONTROL_POLICY"
        }
    }
}
```
For more information, see [Creating organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_create.html) in the *AWS Organizations User Guide*.
+  For API details, see [CreatePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-policy.html) in *AWS CLI Command Reference*.

### `decline-handshake`
<a name="organizations_DeclineHandshake_cli_2_topic"></a>

The following code example shows how to use `decline-handshake`.

**AWS CLI**
**To decline a handshake sent from another account**
The following `decline-handshake` example declines an invitation to join Bill's organization on behalf of Susan, an admin who is the owner of account 222222222222. The DeclineHandshake operation returns a handshake object, showing that the state is now DECLINED.

```
aws organizations decline-handshake \
    --handshake-id {{h-examplehandshakeid111}}
```
Output:

```
{
    "Handshake": {
        "Id": "h-examplehandshakeid111",
        "State": "DECLINED",
        "Resources": [
            {
                "Type": "ORGANIZATION",
                "Value": "o-exampleorgid",
                "Resources": [
                    {
                        "Type": "MASTER_EMAIL",
                        "Value": "bill@example.com"
                    },
                    {
                        "Type": "MASTER_NAME",
                        "Value": "Master Account"
                    }
                ]
            },
            {
                "Type": "EMAIL",
                "Value": "susan@example.com"
            },
            {
                "Type": "NOTES",
                "Value": "This is an invitation to Susan's account to join the Bill's organization."
            }
        ],
        "Parties": [
            {
                "Type": "EMAIL",
                "Id": "susan@example.com"
            },
            {
                "Type": "ORGANIZATION",
                "Id": "o-exampleorgid"
            }
        ],
        "Action": "INVITE",
        "RequestedTimestamp": 1470684478.687,
        "ExpirationTimestamp": 1471980478.687,
        "Arn": "arn:aws:organizations::123456789012:handshake/o-exampleorgid/invite/h-examplehandshakeid111"
    }
}
```
For more information, see [Accepting or declining account invitations with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_accept-decline-invite.html) in the *AWS Organizations User Guide*.
+  For API details, see [DeclineHandshake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/decline-handshake.html) in *AWS CLI Command Reference*.

### `delete-organization`
<a name="organizations_DeleteOrganization_cli_2_topic"></a>

The following code example shows how to use `delete-organization`.

**AWS CLI**
**To delete an organization**
The following `delete-organization` example deletes an organization. To perform this operation, you must be an admin of the master account in the organization. The example assumes that you previously removed all the member accounts, OUs, and policies from the organization.

```
aws organizations delete-organization
```
This command produces no output.
For more information, see [Deleting an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_delete.html) in the *AWS Organizations User Guide*.
+  For API details, see [DeleteOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organization.html) in *AWS CLI Command Reference*.

### `delete-organizational-unit`
<a name="organizations_DeleteOrganizationalUnit_cli_2_topic"></a>

The following code example shows how to use `delete-organizational-unit`.

**AWS CLI**
**To delete an OU**
The following `delete-organizational-unit` example deletes an OU. The example assumes that you previously removed all accounts and other OUs from the OU.

```
aws organizations delete-organizational-unit \
    --organizational-unit-id {{ou-examplerootid111-exampleouid111}}
```
This command produces no output.
For more information, see [Deleting an organizational unit (OU) with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/delete-ou.html) in the *AWS Organizations User Guide*.
+  For API details, see [DeleteOrganizationalUnit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organizational-unit.html) in *AWS CLI Command Reference*.

### `delete-policy`
<a name="organizations_DeletePolicy_cli_2_topic"></a>

The following code example shows how to use `delete-policy`.

**AWS CLI**
**To delete a policy**
The following `delete-policy` example deletes a policy from an organization. The example assumes that you previously detached the policy from all entities.

```
aws organizations delete-policy \
    --policy-id {{p-examplepolicyid111}}
```
This command produces no output.
For more information, see [Deleting organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_delete.html) in the *AWS Organizations User Guide*.
+  For API details, see [DeletePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-policy.html) in *AWS CLI Command Reference*.

### `describe-account`
<a name="organizations_DescribeAccount_cli_2_topic"></a>

The following code example shows how to use `describe-account`.

**AWS CLI**
**To get the details about an account**
The following `describe-account` example requests details about an account.

```
aws organizations describe-account \
    --account-id {{123456789444}}
```
Output:

```
{
    "Account": {
        "Id": "123456789444",
        "Arn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789444",
        "Name": "Beta account",
        "Email": "anika@example.com",
        "JoinedMethod": "INVITED",
        "JoinedTimestamp": 1481756563.134,
        "Paths": [
            "o-exampleorgid/r-examplerootid111/123456789444/"
        ],
        "State": "ACTIVE",
        "Status": "ACTIVE"
    }
}
```
For more information, see [View details of an account in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_account.html) in the *AWS Organizations User Guide*.
+  For API details, see [DescribeAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-account.html) in *AWS CLI Command Reference*.

### `describe-create-account-status`
<a name="organizations_DescribeCreateAccountStatus_cli_2_topic"></a>

The following code example shows how to use `describe-create-account-status`.

**AWS CLI**
**To get the latest status about a request to create an account**
The following `describe-create-account-status` example requests the latest status for a previous request to create an account in an organization. The specified `--create-account-request-id` comes from the response of the original call to create-account. The account creation request shows by the status field that Organizations successfully completed the creation of the account.

```
aws organizations describe-create-account-status \
    --create-account-request-id {{car-examplecreateaccountrequestid111}}
```
Output:

```
{
    "CreateAccountStatus": {
        "State": "SUCCEEDED",
        "AccountId": "123456789444",
        "AccountName": "Beta account",
        "RequestedTimestamp": 1470684478.687,
        "CompletedTimestamp": 1470684532.472,
        "Id": "car-examplecreateaccountrequestid111"
    }
}
```
For more information, see [Creating a member account in an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) in the *AWS Organizations User Guide*.
+  For API details, see [DescribeCreateAccountStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-create-account-status.html) in *AWS CLI Command Reference*.

### `describe-handshake`
<a name="organizations_DescribeHandshake_cli_2_topic"></a>

The following code example shows how to use `describe-handshake`.

**AWS CLI**
**To get information about a handshake**
The following `describe-handshake` example requests details about a handshake. The handshake ID comes either from the original call to `InviteAccountToOrganization`, or from a call to `ListHandshakesForAccount` or `ListHandshakesForOrganization`.

```
aws organizations describe-handshake \
    --handshake-id {{h-examplehandshakeid111}}
```
Output:

```
{
    "Handshake": {
        "Id": "h-examplehandshakeid111",
        "State": "OPEN",
        "Resources": [
            {
                "Type": "ORGANIZATION",
                "Value": "o-exampleorgid",
                "Resources": [
                    {
                        "Type": "MASTER_EMAIL",
                        "Value": "bill@example.com"
                    },
                    {
                        "Type": "MASTER_NAME",
                        "Value": "Master Account"
                    }
                ]
            },
            {
                "Type": "EMAIL",
                "Value": "anika@example.com"
            }
        ],
        "Parties": [
            {
                "Type": "ORGANIZATION",
                "Id": "o-exampleorgid"
            },
            {
                "Type": "EMAIL",
                "Id": "anika@example.com"
            }
        ],
        "Action": "INVITE",
        "RequestedTimestamp": 1470158698.046,
        "ExpirationTimestamp": 1471454698.046,
        "Arn": "arn:aws:organizations::123456789012:handshake/o-exampleorgid/invite/h-examplehandshakeid111"
    }
}
```
For more information, see [Managing account invitations with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) in the *AWS Organizations User Guide*.
+  For API details, see [DescribeHandshake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-handshake.html) in *AWS CLI Command Reference*.

### `describe-organization`
<a name="organizations_DescribeOrganization_cli_2_topic"></a>

The following code example shows how to use `describe-organization`.

**AWS CLI**
**To get information about the current organization**
The following `describe-organization` example requests details about an organization.

```
aws organizations describe-organization
```
Output:

```
{
    "Organization": {
        "MasterAccountArn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789012",
        "MasterAccountEmail": "bill@example.com",
        "MasterAccountId": "123456789012",
        "Id": "o-exampleorgid",
        "FeatureSet": "ALL",
        "Arn": "arn:aws:organizations::123456789012:organization/o-exampleorgid",
        "AvailablePolicyTypes": [
            {
                "Status": "ENABLED",
                "Type": "SERVICE_CONTROL_POLICY"
            }
        ]
    }
}
```
For more information, see [Viewing details of an organization from the management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_org.html) in the *AWS Organizations User Guide*.
+  For API details, see [DescribeOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-organization.html) in *AWS CLI Command Reference*.

### `describe-organizational-unit`
<a name="organizations_DescribeOrganizationalUnit_cli_2_topic"></a>

The following code example shows how to use `describe-organizational-unit`.

**AWS CLI**
**To get information about an OU**
The following `describe-organizational-unit` example requests details about an OU.

```
aws organizations describe-organizational-unit \
    --organizational-unit-id {{ou-examplerootid111-exampleouid111}}
```
Output:

```
{
    "OrganizationalUnit": {
        "Name": "Accounting Group",
        "Arn": "arn:aws:organizations::123456789012:ou/o-exampleorgid/ou-examplerootid111-exampleouid111",
        "Id": "ou-examplerootid111-exampleouid111"
    }
}
```
For more information, see [Viewing details of an organizational unit (OU) with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_ou.html) in the *AWS Organizations User Guide*.
+  For API details, see [DescribeOrganizationalUnit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-organizational-unit.html) in *AWS CLI Command Reference*.

### `describe-policy`
<a name="organizations_DescribePolicy_cli_2_topic"></a>

The following code example shows how to use `describe-policy`.

**AWS CLI**
**To get information about a policy**
The following `describe-policy` example requests information about a policy.

```
aws organizations describe-policy \
    --policy-id {{p-examplepolicyid111}}
```
Output:

```
{
    "Policy": {
        "Content": "{\n  \"Version\": \"2012-10-17\",\n  \"Statement\": [\n    {\n      \"Effect\": \"Allow\",\n      \"Action\": \"*\",\n      \"Resource\": \"*\"\n    }\n  ]\n}",
        "PolicySummary": {
            "Arn": "arn:aws:organizations::123456789012:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111",
            "Type": "SERVICE_CONTROL_POLICY",
            "Id": "p-examplepolicyid111",
            "AwsManaged": false,
            "Name": "AllowAllS3Actions",
            "Description": "Enables admins to delegate S3 permissions"
        }
    }
}
```
For more information, see [Getting information about your organization's policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_info-operations.html) in the *AWS Organizations User Guide*.
+  For API details, see [DescribePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-policy.html) in *AWS CLI Command Reference*.

### `detach-policy`
<a name="organizations_DetachPolicy_cli_2_topic"></a>

The following code example shows how to use `detach-policy`.

**AWS CLI**
**To detach a policy from a root, OU, or account**
The following `detach-policy` example detaches a policy from an OU.

```
aws organizations detach-policy \
    --target-id {{ou-examplerootid111-exampleouid111}} \
    --policy-id {{p-examplepolicyid111}}
```
This command produces no output.
For more information, see [Detaching organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_detach.html) in the *AWS Organizations User Guide*.
+  For API details, see [DetachPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/detach-policy.html) in *AWS CLI Command Reference*.

### `disable-policy-type`
<a name="organizations_DisablePolicyType_cli_2_topic"></a>

The following code example shows how to use `disable-policy-type`.

**AWS CLI**
**To disable a policy type in a root**
The following `disable-policy-type` example disables the service control policy (SCP) policy type in a root. The output shows that the `PolicyTypes` response element no longer includes `SERVICE_CONTROL_POLICY`.

```
aws organizations disable-policy-type \
    --root-id {{r-examplerootid111}} \
    --policy-type {{SERVICE_CONTROL_POLICY}}
```
Output:

```
{
    "Root": {
        "PolicyTypes": [],
        "Name": "Root",
        "Id": "r-examplerootid111",
        "Arn": "arn:aws:organizations::123456789012:root/o-exampleorgid/r-examplerootid111"
    }
}
```
For more information, see [Disabling a policy type](https://docs.aws.amazon.com/organizations/latest/userguide/disable-policy-type.html) in the *AWS Organizations User Guide*.
+  For API details, see [DisablePolicyType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/disable-policy-type.html) in *AWS CLI Command Reference*.

### `enable-all-features`
<a name="organizations_EnableAllFeatures_cli_2_topic"></a>

The following code example shows how to use `enable-all-features`.

**AWS CLI**
**To enable all features in an organization**
The following `enable-all-features` example asks all the invited accounts in the organization to approve enabling all features in the organization. AWS Organizations sends an email to the address that is registered with every invited member account asking the owner to approve the change to all features by accepting the handshake that is sent. After all invited member accounts accept the handshake, the organization administrator can finalize the change to all features, and those with appropriate permissions can create policies and apply them to roots, OUs, and accounts.

```
aws organizations enable-all-features
```
The output is a handshake object that is sent to all invited member accounts for approval.
Output:

```
{
    "Handshake": {
        "Action": "ENABLE_ALL_FEATURES",
        "Arn": "arn:aws:organizations::123456789012:handshake/o-exampleorgid/enable_all_features/h-examplehandshakeid111",
        "ExpirationTimestamp": 1483127868.609,
        "Id": "h-examplehandshakeid111",
        "Parties": [
            {
                "Id": "o-exampleorgid",
                "Type": "ORGANIZATION"
            }
        ],
        "RequestedTimestamp": 1481831868.609,
        "Resources": [
            {
                "Type": "ORGANIZATION",
                "Value": "o-exampleorgid"
            }
        ],
        "State": "REQUESTED"
    }
}
```
For more information, see [Enabling all features for an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.
+  For API details, see [EnableAllFeatures](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-all-features.html) in *AWS CLI Command Reference*.

### `enable-policy-type`
<a name="organizations_EnablePolicyType_cli_2_topic"></a>

The following code example shows how to use `enable-policy-type`.

**AWS CLI**
**To enable the use of a policy type in a root**
The following `enable-policy-type` example enables the service control policy (SCP) policy type in a root.

```
aws organizations enable-policy-type \
    --root-id {{r-examplerootid111}} \
    --policy-type {{SERVICE_CONTROL_POLICY}}
```
The output shows a root object with a policyTypes response element showing that SCPs are now enabled.
Output:

```
{
    "Root": {
        "PolicyTypes": [
            {
                "Status": "ENABLED",
                "Type": "SERVICE_CONTROL_POLICY"
            }
        ],
        "Id": "r-examplerootid111",
        "Name": "Root",
        "Arn": "arn:aws:organizations::123456789012:root/o-exampleorgid/r-examplerootid111"
    }
}
```
For more information, see [Enabling a policy type](https://docs.aws.amazon.com/organizations/latest/userguide/enable-policy-type.html) in the *AWS Organizations User Guide*.
+  For API details, see [EnablePolicyType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-policy-type.html) in *AWS CLI Command Reference*.

### `invite-account-to-organization`
<a name="organizations_InviteAccountToOrganization_cli_2_topic"></a>

The following code example shows how to use `invite-account-to-organization`.

**AWS CLI**
**To invite an account to join an organization**
The following `invite-account-to-organization` example invites the account owned by juan@example.com to join an organization from the master account owned by bill@example.com.

```
aws organizations invite-account-to-organization \
    --target '{{{"Type": "EMAIL", "Id": "juan@example.com"}}}' \
    --notes {{"This is a request for Juan's account to join Bill's organization."}}
```
The output includes a handshake structure that shows what is sent to the invited account.
Output:

```
{
    "Handshake": {
        "Action": "INVITE",
        "Arn": "arn:aws:organizations::123456789012:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
        "ExpirationTimestamp": 1482952459.257,
        "Id": "h-examplehandshakeid111",
        "Parties": [
            {
                "Id": "o-exampleorgid",
                "Type": "ORGANIZATION"
            },
            {
                "Id": "juan@example.com",
                "Type": "EMAIL"
            }
        ],
        "RequestedTimestamp": 1481656459.257,
        "Resources": [
            {
                "Resources": [
                    {
                        "Type": "MASTER_EMAIL",
                        "Value": "bill@amazon.com"
                    },
                    {
                        "Type": "MASTER_NAME",
                        "Value": "Org Master Account"
                    },
                    {
                        "Type": "ORGANIZATION_FEATURE_SET",
                        "Value": "FULL"
                    }
                ],
                "Type": "ORGANIZATION",
                "Value": "o-exampleorgid"
            },
            {
                "Type": "EMAIL",
                "Value": "juan@example.com"
            }
        ],
        "State": "OPEN"
    }
}
```
For more information, see [Managing account invitations with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) in the *AWS Organizations User Guide*.
+  For API details, see [InviteAccountToOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/invite-account-to-organization.html) in *AWS CLI Command Reference*.

### `leave-organization`
<a name="organizations_LeaveOrganization_cli_2_topic"></a>

The following code example shows how to use `leave-organization`.

**AWS CLI**
**To leave an organization as a member account**
The following `leave-organization` example requests that a member account leave the organization it is currently a member of.

```
aws organizations leave-organization
```
This command produces no output.
For more information, see [Leaving an organization from a member account with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_leave-as-member.html) in the *AWS Organizations User Guide*.
+  For API details, see [LeaveOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/leave-organization.html) in *AWS CLI Command Reference*.

### `list-accounts-for-parent`
<a name="organizations_ListAccountsForParent_cli_2_topic"></a>

The following code example shows how to use `list-accounts-for-parent`.

**AWS CLI**
**To retrieve a list of all of the accounts in a specified parent root or OU**
The following `list-accounts-for-parent` example requests a list of the accounts in an OU.

```
aws organizations list-accounts-for-parent \
    --parent-id {{ou-examplerootid111-exampleouid111}}
```
The output includes a list of account summary objects.
Output:

```
{
    "Accounts": [
        {
            "Arn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789222",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481835795.536,
            "Id": "123456789222",
            "Name": "Development Account",
            "Email": "juan@example.com",
            "Paths": [
                "o-exampleorgid/r-examplerootid111/123456789012/"
            ],
            "State": "ACTIVE",
            "Status": "ACTIVE"
        },
        {
            "Arn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789333",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481835812.143,
            "Id": "123456789333",
            "Name": "Test Account",
            "Email": "anika@example.com",
            "Paths": [
                "o-exampleorgid/r-examplerootid111/123456789012/"
            ],
            "State": "ACTIVE",
            "Status": "ACTIVE"
        }
    ]
}
```
For more information, see [Managing accounts in an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListAccountsForParent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-accounts-for-parent.html) in *AWS CLI Command Reference*.

### `list-accounts`
<a name="organizations_ListAccounts_cli_2_topic"></a>

The following code example shows how to use `list-accounts`.

**AWS CLI**
**To retrieve a list of all of the accounts in an organization**
The following `list-accounts` example requests a list of the accounts in an organization.

```
aws organizations list-accounts
```
The output includes a list of account summary objects.
Output:

```
{
    "Accounts": [
        {
            "Arn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789012",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481830215.45,
            "Id": "123456789012",
            "Name": "Master Account",
            "Email": "bill@example.com",
            "Paths": [
                "o-exampleorgid/r-examplerootid111/123456789012/"
            ],
            "State": "ACTIVE",
            "Status": "ACTIVE"
        },
        {
            "Arn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789111",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481835741.044,
            "Id": "123456789111",
            "Name": "Production Account",
            "Email": "alice@example.com",
            "Paths": [
                "o-exampleorgid/r-examplerootid111/123456789012/"
            ],
            "State": "ACTIVE",
            "Status": "ACTIVE"
        },
        {
            "Arn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789222",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481835795.536,
            "Id": "123456789222",
            "Name": "Development Account",
            "Email": "juan@example.com",
            "Paths": [
                "o-exampleorgid/r-examplerootid111/123456789012/"
            ],
            "State": "ACTIVE",
            "Status": "ACTIVE"
        },
        {
            "Arn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789333",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481835812.143,
            "Id": "123456789333",
            "Name": "Test Account",
            "Email": "anika@example.com",
            "Paths": [
                "o-exampleorgid/r-examplerootid111/123456789012/"
            ],
            "State": "ACTIVE",
            "Status": "ACTIVE"
        }
    ]
}
```
For more information, see [Managing accounts in an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListAccounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-accounts.html) in *AWS CLI Command Reference*.

### `list-children`
<a name="organizations_ListChildren_cli_2_topic"></a>

The following code example shows how to use `list-children`.

**AWS CLI**
**To retrieve the child accounts and OUs of a parent OU or root**
The following `list-children` example lists the child OUs of a parent OU.

```
aws organizations list-children \
    --child-type {{ORGANIZATIONAL_UNIT}} \
    --parent-id {{ou-examplerootid111-exampleouid111}}
```
The output shows the two child OUs that are contained by the parent.
Output:

```
{
    "Children": [
        {
            "Id": "ou-examplerootid111-exampleouid111",
            "Type": "ORGANIZATIONAL_UNIT"
        },
        {
            "Id": "ou-examplerootid111-exampleouid222",
            "Type": "ORGANIZATIONAL_UNIT"
        }
    ]
}
```
For more information, see [Managing organizational units (OUs) with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListChildren](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-children.html) in *AWS CLI Command Reference*.

### `list-create-account-status`
<a name="organizations_ListCreateAccountStatus_cli_2_topic"></a>

The following code example shows how to use `list-create-account-status`.

**AWS CLI**
**Example 1: To retrieve a list of the account creation requests made in the current organization**
The following `list-create-account-status` example requests a list of account creation requests for an organization that have completed successfully.

```
aws organizations list-create-account-status \
    --states {{SUCCEEDED}}
```
The output includes an array of objects with information about each request.
Output:

```
{
    "CreateAccountStatuses": [
        {
            "AccountId": "123456789333",
            "AccountName": "Developer Test Account",
            "CompletedTimestamp": 1481835812.143,
            "Id": "car-examplecreateaccountrequestid111",
            "RequestedTimestamp": 1481829432.531,
            "State": "SUCCEEDED"
        }
    ]
}
```
For more information, see [Creating a member account in an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) in the *AWS Organizations User Guide*.
**Example 2: To retrieve a list of the in progress account creation requests made in the current organization**
The following `list-create-account-status` example gets a list of in-progress account creation requests for an organization.

```
aws organizations list-create-account-status \
    --states {{IN_PROGRESS}}
```
The output includes an array of objects with information about each request.
Output:

```
{
    "CreateAccountStatuses": [
        {
            "State": "IN_PROGRESS",
            "Id": "car-examplecreateaccountrequestid111",
            "RequestedTimestamp": 1481829432.531,
            "AccountName": "Production Account"
        }
    ]
}
```
For more information, see [Creating a member account in an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListCreateAccountStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-create-account-status.html) in *AWS CLI Command Reference*.

### `list-handshakes-for-account`
<a name="organizations_ListHandshakesForAccount_cli_2_topic"></a>

The following code example shows how to use `list-handshakes-for-account`.

**AWS CLI**
**To retrieve a list of the handshakes sent to an account**
The following `list-handshakes-for-account` example gets a list of all handshakes that are associated with the account of the credentials that were used to call the operation.

```
aws organizations list-handshakes-for-account
```
The output includes a list of handshake structures with information about each handshake including its current state.
Output:

```
{
    "Handshakes": [
        {
        "Action": "INVITE",
        "Arn": "arn:aws:organizations::123456789012:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
        "ExpirationTimestamp": 1482952459.257,
        "Id": "h-examplehandshakeid111",
        "Parties": [
            {
                "Id": "o-exampleorgid",
                "Type": "ORGANIZATION"
            },
            {
                "Id": "juan@example.com",
                "Type": "EMAIL"
            }
        ],
        "RequestedTimestamp": 1481656459.257,
        "Resources": [
            {
                "Resources": [
                    {
                        "Type": "MASTER_EMAIL",
                        "Value": "bill@amazon.com"
                    },
                    {
                        "Type": "MASTER_NAME",
                        "Value": "Org Master Account"
                    },
                    {
                        "Type": "ORGANIZATION_FEATURE_SET",
                        "Value": "FULL"
                    }
                ],
                "Type": "ORGANIZATION",
                "Value": "o-exampleorgid"
            },
            {
                "Type": "EMAIL",
                "Value": "juan@example.com"
            }
        ],
        "State": "OPEN"
    }
    ]
}
```
For more information, see [Managing account invitations with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListHandshakesForAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-handshakes-for-account.html) in *AWS CLI Command Reference*.

### `list-handshakes-for-organization`
<a name="organizations_ListHandshakesForOrganization_cli_2_topic"></a>

The following code example shows how to use `list-handshakes-for-organization`.

**AWS CLI**
**To retrieve a list of the handshakes associated with an organization**
The following `list-handshakes-for-organization` example gets a list of handshakes that are associated with the current organization.

```
aws organizations list-handshakes-for-organization
```
The output shows two handshakes. The first one is an invitation to Juan's account and shows a state of OPEN. The second is an invitation to Anika's account and shows a state of ACCEPTED.
Output:

```
{
    "Handshakes": [
        {
            "Action": "INVITE",
            "Arn": "arn:aws:organizations::123456789012:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
            "ExpirationTimestamp": 1482952459.257,
            "Id": "h-examplehandshakeid111",
            "Parties": [
                {
                    "Id": "o-exampleorgid",
                    "Type": "ORGANIZATION"
                },
                {
                    "Id": "juan@example.com",
                    "Type": "EMAIL"
                }
            ],
            "RequestedTimestamp": 1481656459.257,
            "Resources": [
                {
                    "Resources": [
                        {
                            "Type": "MASTER_EMAIL",
                            "Value": "bill@amazon.com"
                        },
                        {
                            "Type": "MASTER_NAME",
                            "Value": "Org Master Account"
                        },
                        {
                            "Type": "ORGANIZATION_FEATURE_SET",
                            "Value": "FULL"
                        }
                    ],
                    "Type": "ORGANIZATION",
                    "Value": "o-exampleorgid"
                },
                {
                    "Type": "EMAIL",
                    "Value": "juan@example.com"
                },
                {
                    "Type": "NOTES",
                    "Value": "This is an invitation to Juan's account to join Bill's organization."
                }
            ],
            "State": "OPEN"
        },
        {
            "Action": "INVITE",
            "State": "ACCEPTED",
            "Arn": "arn:aws:organizations::123456789012:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
            "ExpirationTimestamp": 1471797437.427,
            "Id": "h-examplehandshakeid222",
            "Parties": [
                {
                    "Id": "o-exampleorgid",
                    "Type": "ORGANIZATION"
                },
                {
                    "Id": "anika@example.com",
                    "Type": "EMAIL"
                }
            ],
            "RequestedTimestamp": 1469205437.427,
            "Resources": [
                {
                    "Resources": [
                        {
                            "Type": "MASTER_EMAIL",
                            "Value": "bill@example.com"
                        },
                        {
                            "Type": "MASTER_NAME",
                            "Value": "Master Account"
                        }
                    ],
                    "Type": "ORGANIZATION",
                    "Value": "o-exampleorgid"
                },
                {
                    "Type": "EMAIL",
                    "Value": "anika@example.com"
                },
                {
                    "Type": "NOTES",
                    "Value": "This is an invitation to Anika's account to join Bill's organization."
                }
            ]
        }
    ]
}
```
For more information, see [Managing account invitations with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListHandshakesForOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-handshakes-for-organization.html) in *AWS CLI Command Reference*.

### `list-organizational-units-for-parent`
<a name="organizations_ListOrganizationalUnitsForParent_cli_2_topic"></a>

The following code example shows how to use `list-organizational-units-for-parent`.

**AWS CLI**
**To retrieve a list of the OUs in a parent OU or root**
The following `list-organizational-units-for-parent` example gets a list of OUs in a specified root.

```
aws organizations list-organizational-units-for-parent \
    --parent-id {{r-examplerootid111}}
```
The output shows that the specified root contains two OUs and shows details of each.
Output:

```
{
    "OrganizationalUnits": [
        {
            "Name": "AccountingDepartment",
            "Arn": "arn:aws:organizations::o-exampleorgid:ou/r-examplerootid111/ou-examplerootid111-exampleouid111"
        },
        {
            "Name": "ProductionDepartment",
            "Arn": "arn:aws:organizations::o-exampleorgid:ou/r-examplerootid111/ou-examplerootid111-exampleouid222"
        }
    ]
}
```
For more information, see [Managing organizational units (OUs) with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListOrganizationalUnitsForParent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-organizational-units-for-parent.html) in *AWS CLI Command Reference*.

### `list-parents`
<a name="organizations_ListParents_cli_2_topic"></a>

The following code example shows how to use `list-parents`.

**AWS CLI**
**To list the parent OUs or roots for an account or child OU**
The following `list-parents` example lists the root or parent OU that contains the account 444444444444.

```
aws organizations list-parents \
    --child-id {{123456789333}}
```
The output shows that the specified account is in the OU with specified ID.
Output:

```
{
    "Parents": [
        {
            "Id": "ou-examplerootid111-exampleouid111",
            "Type": "ORGANIZATIONAL_UNIT"
        }
    ]
}
```
For more information, see [Managing organizational units (OUs) with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListParents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-parents.html) in *AWS CLI Command Reference*.

### `list-policies-for-target`
<a name="organizations_ListPoliciesForTarget_cli_2_topic"></a>

The following code example shows how to use `list-policies-for-target`.

**AWS CLI**
**To retrieve a list of the SCPs attached directly to an account**
The following `list-policies-for-target` example gets a list of all service control policies (SCPs), as specified by the `--filter` parameter, that are directly attached to an account.

```
aws organizations list-policies-for-target \
    --filter {{SERVICE_CONTROL_POLICY}} \
    --target-id {{123456789333}}
```
The output includes a list of policy structures with summary information about the policies. The list does not include policies that apply to the account because of inheritance from its location in an OU hierarchy.
Output:

```
{
    "Policies": [
        {
            "Type": "SERVICE_CONTROL_POLICY",
            "Name": "AllowAllEC2Actions",
            "AwsManaged": false,
            "Id": "p-examplepolicyid222",
            "Arn": "arn:aws:organizations::o-exampleorgid:policy/service_control_policy/p-examplepolicyid222",
            "Description": "Enables account admins to delegate permissions for any EC2 actions to users and roles in their accounts."
        }
    ]
}
```
For more information, see [Getting information about your organization's policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_info-operations.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListPoliciesForTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies-for-target.html) in *AWS CLI Command Reference*.

### `list-policies`
<a name="organizations_ListPolicies_cli_2_topic"></a>

The following code example shows how to use `list-policies`.

**AWS CLI**
**To retrieve a list of all policies in an organization of a certain type**
The following `list-policies` example gets a list of SCPs, as specified by the `--filter` parameter.

```
aws organizations list-policies \
    --filter {{SERVICE_CONTROL_POLICY}}
```
The output includes a list of policies with summary information.
Output:

```
{
    "Policies": [
        {
            "Type": "SERVICE_CONTROL_POLICY",
            "Name": "AllowAllS3Actions",
            "AwsManaged": false,
            "Id": "p-examplepolicyid111",
            "Arn": "arn:aws:organizations::123456789012:policy/service_control_policy/p-examplepolicyid111",
            "Description": "Enables account admins to delegate permissions for any S3 actions to users and roles in their accounts."
        },
        {
            "Type": "SERVICE_CONTROL_POLICY",
            "Name": "AllowAllEC2Actions",
            "AwsManaged": false,
            "Id": "p-examplepolicyid222",
            "Arn": "arn:aws:organizations::123456789012:policy/service_control_policy/p-examplepolicyid222",
            "Description": "Enables account admins to delegate permissions for any EC2 actions to users and roles in their accounts."
        },
        {
            "AwsManaged": true,
            "Description": "Allows access to every operation",
            "Type": "SERVICE_CONTROL_POLICY",
            "Id": "p-FullAWSAccess",
            "Arn": "arn:aws:organizations::aws:policy/service_control_policy/p-FullAWSAccess",
            "Name": "FullAWSAccess"
        }
    ]
}
```
For more information, see [Getting information about your organization's policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_info-operations.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies.html) in *AWS CLI Command Reference*.

### `list-roots`
<a name="organizations_ListRoots_cli_2_topic"></a>

The following code example shows how to use `list-roots`.

**AWS CLI**
**To retrieve a list of the roots in an organization**
The following `list-roots` example gets the list of roots for an organization.

```
aws organizations list-roots
```
The output includes a list of root structures with summary information.
Output:

```
{
    "Roots": [
        {
            "Name": "Root",
            "Arn": "arn:aws:organizations::123456789012:root/o-exampleorgid/r-examplerootid111",
            "Id": "r-examplerootid111",
            "PolicyTypes": [
                {
                    "Status": "ENABLED",
                    "Type": "SERVICE_CONTROL_POLICY"
                }
            ]
        }
    ]
}
```
For more information, see [Terminology and concepts for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListRoots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-roots.html) in *AWS CLI Command Reference*.

### `list-targets-for-policy`
<a name="organizations_ListTargetsForPolicy_cli_2_topic"></a>

The following code example shows how to use `list-targets-for-policy`.

**AWS CLI**
**To retrieve a list of the roots, OUs, and accounts that a policy is attached to**
The following `list-targets-for-policy` example gets a list of the roots, OUs, and accounts that the specified policy is attached to. The output includes a list of attachment objects with summary information about the roots, OUs, and accounts the policy is attached to.

```
aws organizations list-targets-for-policy \
    --policy-id {{p-FullAWSAccess}}
```
Output:

```
{
    "Targets": [
        {
            "Arn": "arn:aws:organizations::123456789012:root/o-exampleorgid/r-examplerootid111",
            "Name": "Root",
            "TargetId": "r-examplerootid111",
            "Type": "ROOT"
        },
        {
            "Arn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789222",
            "Name": "Developer Test Account",
            "TargetId": "123456789222",
            "Type": "ACCOUNT"
        },
        {
            "Arn": "arn:aws:organizations::123456789012:ou/o-exampleorgid/ou-examplerootid111-exampleouid111",
            "Name": "Accounting",
            "TargetId": "ou-examplerootid111-exampleouid111",
            "Type": "ORGANIZATIONAL_UNIT"
        }
    ]
}
```
For more information, see [Getting information about your organization's policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_info-operations.html) in the *AWS Organizations User Guide*.
+  For API details, see [ListTargetsForPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-targets-for-policy.html) in *AWS CLI Command Reference*.

### `move-account`
<a name="organizations_MoveAccount_cli_2_topic"></a>

The following code example shows how to use `move-account`.

**AWS CLI**
**To move an account between roots or OUs**
The following `move-account` example moves the management account in the organization from the root to an OU.

```
aws organizations move-account \
    --account-id {{123456789222}} \
    --source-parent-id {{r-examplerootid111}} \
    --destination-parent-id {{ou-examplerootid111-exampleouid111}}
```
This command produces no output.
For more information, see [Moving accounts to an organizational unit (OU) or between the root and OUs with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/move_account_to_ou.html) in the *AWS Organizations User Guide*.
+  For API details, see [MoveAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/move-account.html) in *AWS CLI Command Reference*.

### `remove-account-from-organization`
<a name="organizations_RemoveAccountFromOrganization_cli_2_topic"></a>

The following code example shows how to use `remove-account-from-organization`.

**AWS CLI**
**To remove an account from an organization as the master account**
The following `remove-account-from-organization` example removes an account from an organization.

```
aws organizations remove-account-from-organization \
    --account-id {{123456789222}}
```
This command produces no output.
For more information, see [Removing a member account from an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html) in the *AWS Organizations User Guide*.
+  For API details, see [RemoveAccountFromOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/remove-account-from-organization.html) in *AWS CLI Command Reference*.

### `update-organizational-unit`
<a name="organizations_UpdateOrganizationalUnit_cli_2_topic"></a>

The following code example shows how to use `update-organizational-unit`.

**AWS CLI**
**To rename an OU**
The following `update-organizational-unit` example renames an OU to `AccountingOU`. The output shows the new name.

```
aws organizations update-organizational-unit \
    --organizational-unit-id {{ou-examplerootid111-exampleouid111}} \
    --name {{AccountingOU}}
```
Output:

```
{
    "OrganizationalUnit": {
        "Id": "ou-examplerootid111-exampleouid111",
        "Name": "AccountingOU",
        "Arn": "arn:aws:organizations::123456789012:ou/o-exampleorgid/ou-examplerootid111-exampleouid111"
    }
}
```
For more information, see [Managing organizational units (OUs) with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) in the *AWS Organizations User Guide*.
+  For API details, see [UpdateOrganizationalUnit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/update-organizational-unit.html) in *AWS CLI Command Reference*.

### `update-policy`
<a name="organizations_UpdatePolicy_cli_2_topic"></a>

The following code example shows how to use `update-policy`.

**AWS CLI**
**Example 1: To rename a policy**
The following `update-policy` example renames a policy and gives it a new description. The output shows the new name and description.

```
aws organizations update-policy \
    --policy-id {{p-examplepolicyid111}} \
    --name {{Renamed-Policy}} \
    --description {{"This description replaces the original."}}
```
Output:

```
{
    "Policy": {
        "Content": "{\n  \"Version\":\"2012-10-17\",\n  \"Statement\":{\n    \"Effect\":\"Allow\",\n    \"Action\":\"ec2:*\",\n    \"Resource\":\"*\"\n  }\n}\n",
        "PolicySummary": {
            "Id": "p-examplepolicyid111",
            "AwsManaged": false,
            "Arn": "arn:aws:organizations::123456789012:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111",
            "Description": "This description replaces the original.",
            "Name": "Renamed-Policy",
            "Type": "SERVICE_CONTROL_POLICY"
        }
    }
}
```
For more information, see [Updating organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_update.html) in the *AWS Organizations User Guide*.
**Example 2: To replace a policy's JSON text content**
The following `update-policy` example replaces the JSON text of the SCP in the previous example with a new JSON policy text string that allows S3 instead of EC2. The output shows the new content.

```
aws organizations update-policy \
    --policy-id {{p-examplepolicyid111}} \
    --content "{\"Version\":\"2012-10-17\",\"Statement\":{\"Effect\":\"Allow\",\"Action\":\"s3:*\",\"Resource\":\"*\"}}"
```
Output:

```
{
    "Policy": {
        "Content": "{ \"Version\": \"2012-10-17\", \"Statement\": { \"Effect\": \"Allow\", \"Action\": \"s3:*\", \"Resource\": \"*\" } }",
        "PolicySummary": {
            "Arn": "arn:aws:organizations::123456789012:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111",
            "AwsManaged": false,
            "Description": "This description replaces the original.",
            "Id": "p-examplepolicyid111",
            "Name": "Renamed-Policy",
            "Type": "SERVICE_CONTROL_POLICY"
        }
    }
}
```
For more information, see [Updating organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_update.html) in the *AWS Organizations User Guide*.
+  For API details, see [UpdatePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/update-policy.html) in *AWS CLI Command Reference*.
