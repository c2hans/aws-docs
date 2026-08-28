---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/support-check.html
---

# Checking for support before offering a filter for the Amazon Chime SDK
<a name="support-check"></a>

The Amazon Chime SDK provides an asynchronous static method that checks for supported browsers and attempts to download the required assets. However, it does not check for device performance. As a best practice, always ensure the users' browsers and devices can support the filters before you offer the filters.

```
import {
    VideoFxProcessor
} from 'amazon-chime-sdk-js';

if (!await VideoFxProcessor.isSupported(logger)) {
    // logger is optional for isSupported
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
