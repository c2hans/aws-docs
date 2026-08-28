---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/interactions.html
---

# Interactions in the Connect Customer Flow language
<a name="interactions"></a>

Interactions actions have side effects, but they don't require a contact or a participant. They include actions such as invoking an AWS Lambda function. They generally work in every circumstance.

**Topics**
+ [AssociateContactToCustomerProfile](interactions-associatecontacttocustomerprofile.md)
+ [CreateCallbackContact](interactions-createcallbackcontact.md)
+ [CreateCustomerProfile](interactions-createcustomerprofile.md)
+ [InvokeLambdaFunction](interactions-invokelambdafunction.md)
+ [GetCustomerProfile](interactions-getcustomerprofile.md)
+ [GetCustomerProfileObject](interactions-getcustomerprofileobject.md)
+ [GetCalculatedAttributesForCustomerProfile](interactions-getcalculatedattributesforcustomerprofile.md)
+ [UpdateCustomerProfile](interactions-updatecustomerprofile.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
