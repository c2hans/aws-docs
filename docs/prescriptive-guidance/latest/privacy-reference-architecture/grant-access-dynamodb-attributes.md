---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/grant-access-dynamodb-attributes.html
---

# Grant access to specific Amazon DynamoDB attributes
<a name="grant-access-dynamodb-attributes"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

As your organization discusses strategies to physically and logically separate personal data, consider which AWS storage services support fine-grained access control policies in AWS Identity and Access Management (IAM). The following identity-based policy allows retrieval of only the `UserID`, `SignUpTime`, and `LastLoggedIn` attributes from an Amazon DynamoDB table named `Users`. For example, you might attach this policy to a customer support role instead of giving this role access to the full personal dataset. For more information about how this policy can help protect privacy and personal data in your organization, see [AWS services and features that help segment data](personal-data-account.md#segment-data) in this guide.

```
{
   "Version": "2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "dynamodb:GetItem",
            "dynamodb:BatchGetItem",
            "dynamodb:Query",
            "dynamodb:Scan"
         ],
         "Resource":[
            "arn:aws:dynamodb:us-west-2:123456789012:dynamodb:table/Users"
         ],
         "Condition":{
            "ForAllValues:StringEquals":{
               "dynamodb:Attributes":[
                  "UserID",
                  "SignUpTime",
                  "LastLoggedIn"
               ]
            },
            "StringEquals":{
               "dynamodb:Select":[
                  "SPECIFIC_ATTRIBUTES"
               ]
            }
         }
      }
   ]
}
```
