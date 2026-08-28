---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Contacts.html
---

# Contacts
<a name="API_geoplaces_Contacts"></a>

A list of potential contact methods for the place or result.

## Contents
<a name="API_geoplaces_Contacts_Contents"></a>

 ** Emails **   <a name="location-Type-geoplaces_Contacts-Emails"></a>
List of emails for contacts of the result.
Type: Array of [ContactDetails](API_geoplaces_ContactDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Faxes **   <a name="location-Type-geoplaces_Contacts-Faxes"></a>
List of fax addresses for the result contact.
Type: Array of [ContactDetails](API_geoplaces_ContactDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Phones **   <a name="location-Type-geoplaces_Contacts-Phones"></a>
List of phone numbers for the results contact.
Type: Array of [ContactDetails](API_geoplaces_ContactDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** Websites **   <a name="location-Type-geoplaces_Contacts-Websites"></a>
List of website URLs that belong to the result.
Type: Array of [ContactDetails](API_geoplaces_ContactDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_geoplaces_Contacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/Contacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/Contacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/Contacts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
