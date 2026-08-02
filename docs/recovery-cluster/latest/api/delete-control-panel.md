---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/delete-control-panel.html
---

# Delete a control panel
<a name="delete-control-panel"></a>

The following is an example of a request to delete a control panel. Deleting a control panel doesn't return a response.

```
aws route53-recovery-control-config --region us-west-2 delete-control-panel \
			--control-panel-arn arn:aws:route53-recovery-control::012345678901:controlpanel/aaa123bbb456ccc789aaa123bbb456ccc789
```
