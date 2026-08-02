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
