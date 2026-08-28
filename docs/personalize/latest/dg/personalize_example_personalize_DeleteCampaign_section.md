---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_DeleteCampaign_section.html
---

# Use `DeleteCampaign` with an AWS SDK
<a name="personalize_example_personalize_DeleteCampaign_section"></a>

The following code example shows how to use `DeleteCampaign`.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/personalize#code-examples).

```
    public static void deleteSpecificCampaign(PersonalizeClient personalizeClient, String campaignArn) {
        try {
            DeleteCampaignRequest campaignRequest = DeleteCampaignRequest.builder()
                    .campaignArn(campaignArn)
                    .build();

            personalizeClient.deleteCampaign(campaignRequest);
            System.out.println("Delete request sent successfully.");
        } catch (PersonalizeException e) {
            System.err.println("Error deleting campaign: " + e.awsErrorDetails().errorMessage());
            throw new RuntimeException(e);
        }
    }
}
```
+  For API details, see [DeleteCampaign](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/DeleteCampaign) in *AWS SDK for Java 2.x API Reference*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon Personalize with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
