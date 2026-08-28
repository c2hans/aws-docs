---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/disassociateservicerolefromaccount-delete.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# DisassociateServiceRoleFromAccount
<a name="disassociateservicerolefromaccount-delete"></a>

Disassociates the service role from your account. Without a service role, deployments do not work.

URI: `DELETE /greengrass/servicerole`

## CLI:
<a name="disassociateservicerolefromaccount-delete-cli"></a>

```
aws greengrass disassociate-service-role-from-account  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

## Responses:
<a name="disassociateservicerolefromaccount-delete-resp"></a>

**200**
Success.
 [ DisassociateServiceRoleFromAccountResponse](definitions-disassociateservicerolefromaccountresponse.md)

```
{
"DisassociatedAt": "string"
}
```
DisassociateServiceRoleFromAccountResponse
type: object
DisassociatedAt
The time when the service role was disassociated from the account.
type: string

**500**
Server error.
 [ GeneralError](definitions-generalerror.md)

```
{
"Message": "string",
"ErrorDetails": [
  {
    "DetailedErrorCode": "string",
    "DetailedErrorMessage": "string"
  }
]
}
```
GeneralError
General error information.
type: object
required: ["Message"]
Message
A message that contains information about the error.
type: string
ErrorDetails
A list of error details.
type: array
items: [ErrorDetail](definitions-errordetail.md)
ErrorDetail
Details about the error.
type: object
DetailedErrorCode
A detailed error code.
type: string
DetailedErrorMessage
A detailed error message.
type: string

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
