---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/interactions-getcalculatedattributesforcustomerprofile.html
---

# GetCalculatedAttributesForCustomerProfile
<a name="interactions-getcalculatedattributesforcustomerprofile"></a>

Retrieve calculated attributes for a customer profile. Customer Profiles must be enabled for your Connect Customer instance.

## Parameter object
<a name="getcalculatedattributesforcustomerprofile-parameter"></a>

A `ProfileId` must be present.

```
{
    "ProfileRequestData": {
        "ProfileId": Profile owning the calculated attribute
    },
   "ProfileResponseData": {
       All of these fields are optional.
       "CalculatedAttributes._average_hold_time",
       "CalculatedAttributes._frequent_caller",
       "CalculatedAttributes.x",
   }
}
```

## Results and conditions
<a name="getcalculatedattributesforcustomerprofile-results"></a>

None. Conditions are not supported. If an error does not occur, the response's attributes are available dynamically under the `$.Customer` path based on the attributes included in `ProfileResponseData`.

## Errors
<a name="getcalculatedattributesforcustomerprofile-errors"></a>
+ NoneFoundError - if no profiles were found for the associated profile search key.
+ NoMatchingError - if no other Error matches.

## Corresponding block in the UI
<a name="getcalculatedattributesforcustomerprofile-ui"></a>

[Customer profiles block](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles-block.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
