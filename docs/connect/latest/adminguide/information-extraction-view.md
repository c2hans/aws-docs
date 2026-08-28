---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/information-extraction-view.html
---

# View extracted information
<a name="information-extraction-view"></a>

Extracted information is available in the following locations:
+ **Contact Control Panel (CCP)** – During after-call work
+ **Contact details page** – After the contact ends
+ **Contact search** – Displayed in the contact search results table

## Contact Control Panel (CCP)
<a name="information-extraction-view-ccp"></a>

During the after-call work process, any information extracted with an ACW analysis event source is displayed in the **Extracted Information** widget in the CCP.

![The Extracted Information widget in the Contact Control Panel.](http://docs.aws.amazon.com/connect/latest/adminguide/images/InformationExtraction-View-CCP.png)

## Contact details page
<a name="information-extraction-view-contact-details"></a>

After the contact ends, all extracted information appears in the **Extracted Information** section of the **Contact details** page.

![The Extracted Information section on the Contact details page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/InformationExtraction-View-ContactDetails.png)

## Contact search
<a name="information-extraction-view-contact-search"></a>

Extracted information is displayed in the **Contact search** results table.

![Extracted information displayed in the Contact search results table.](http://docs.aws.amazon.com/connect/latest/adminguide/images/InformationExtraction-View-ContactSearch.png)

## Errors
<a name="information-extraction-errors"></a>

If information extraction fails with a runtime error, the failure is displayed similarly to a category error.

### In the UI (Contact details page)
<a name="information-extraction-errors-ui"></a>

Failed extractions are displayed with dashed borders, transparent backgrounds, and an error icon. Pausing on a failed extraction shows why it failed.

### In the S3 analysis output file
<a name="information-extraction-errors-s3"></a>

Failed extractions appear under `JobDetails.SkippedAnalysis` with the feature `INFORMATION_EXTRACTION` and a reason code:

```
"SkippedAnalysis": [
    {
        "Feature": "INFORMATION_EXTRACTION",
        "ReasonCode": "QUOTA_EXCEEDED",
        "SkippedEntities": [
            { "ExtractionName": "Flight Number", "RuleId": "a113..." }
        ]
    },
    {
        "Feature": "INFORMATION_EXTRACTION",
        "ReasonCode": "FAILED_SAFETY_GUIDELINES",
        "SkippedEntities": [
            { "ExtractionName": "Credit Card Type", "RuleId": "cccc..." }
        ]
    }
]
```

### Common failure reasons
<a name="information-extraction-errors-reasons"></a>

| Reason code | Meaning |
| --- | --- |
| `QUOTA_EXCEEDED` | The AI actions service quota was exceeded at the time of execution. |
| `FAILED_SAFETY_GUIDELINES` | Extraction processing did not satisfy security or quality guardrails. |
| `FEATURE_UNAVAILABLE` | The instance is an Amazon Connect Customer Basic instance, which does not support information extraction. |
| `SYSTEM_ERROR` | An unexpected system error occurred during extraction. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
