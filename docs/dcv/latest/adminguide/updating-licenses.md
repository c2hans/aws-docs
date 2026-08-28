---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/updating-licenses.html
---

# Updating the production license
<a name="updating-licenses"></a>

The Amazon DCV server checks licenses on the RLM server every few minutes. In case the license is updated on the RLM server, Amazon DCV server automatically updates the used license for the running sessions. The following procedure details how to update a DCV license on RLM.

**To update the DCV license on the RLM server**

1. Update the license file which was previously [installed](setting-up-production.md#setting-up-rlm-server). On Linux, it should had been placed in `/opt/dcv/rlm/license/license.lic`, on Windows in `C:\RLM\license\license.lic`.

1. Run `C:\RLM\rlmutil.exe rlmreread` on Windows or `/opt/nice/rlm/rlmutil rlmreread` on Linux to force the license file reload.

 After the license has been updated on the RLM server, the Amazon DCV server should check the use of the new licenses in a few minutes (usually 5 minutes or less).

 Starting from Amazon DCV version 2021.0, you can use the following command **as administrator** in order to force the license update immediately:

```
$ dcv reload-licenses
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
