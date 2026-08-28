---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/interactions-associatecontacttocustomerprofile.html
---

# AssociateContactToCustomerProfile
<a name="interactions-associatecontacttocustomerprofile"></a>

Associate a contact to a customer profile. Customer Profiles must be enabled for your Connect Customer instance.

See [AddProfileKey](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_AddProfileKey.html) in the *Connect Customer Customer Profiles API Reference*.

## Parameter object
<a name="associatecontacttocustomerprofile-parameter"></a>

A `ProfileId` and `ContactId` must be present.

```
{
    "ProfileRequestData": {
        "ProfileId": Profile being associated
        "ContactId": ContactId being associated
    },
   "ProfileResponseData": {
       None.
   }
}
```

## Results and conditions
<a name="associatecontacttocustomerprofile-results"></a>

None. Conditions are not supported.

## Errors
<a name="associatecontacttocustomerprofile-errors"></a>
+ NoMatchingError - if no other Error matches.

## Corresponding block in the UI
<a name="associatecontacttocustomerprofile-ui"></a>

[Customer profiles block](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles-block.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
