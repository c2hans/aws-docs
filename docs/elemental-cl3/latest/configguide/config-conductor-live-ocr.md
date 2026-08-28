---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-ocr.html
---

# Configuring OCR
<a name="config-conductor-live-ocr"></a>

Elemental Live includes a feature that lets you convert captions using OCR conversion. For information about this feature, see [Support for OCR Conversion](https://docs.aws.amazon.com/elemental-live/latest/ug/support-for-ocr.html) in the *AWS Elemental Live User Guide*.

If you want to use this feature, you must enable it. You might have enabled it when you installed the software on the Elemental Live node. If you didn't, you can enable it now using the configuration script (`configure`) instead of the install script. For example:

```
[elemental@hostname ~]$ cd /opt/elemental_se
[elemental@hostname elemental_se]$ sudo ./configure --install-ocr --https --skip-all
```

For complete instructions, see [Install the AWS Elemental Live software](https://docs.aws.amazon.com/elemental-live/latest/installguide/install-lv-ig-install-sw.html) in the *AWS Elemental Live Install Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
