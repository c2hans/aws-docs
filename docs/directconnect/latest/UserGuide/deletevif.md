---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/deletevif.html
---

# Delete a Direct Connect virtual interface
<a name="deletevif"></a>

Delete one or more virtual interfaces. Before you can delete a connection, you must delete its virtual interface. Deleting a virtual interface stops Direct Connect data transfer charges associated with the virtual interface.

You can delete a virtual interface using either the Direct Connect console or the command line or API.

**To delete a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the left pane, choose **Virtual Interfaces**.

1. Select the virtual interfaces and then choose **Delete**.

1. In the **Delete** confirmation dialog box, choose **Delete**.

**To delete a virtual interface using the command line or API**
+ [delete-virtual-interface](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-virtual-interface.html) (AWS CLI)
+ [DeleteVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteVirtualInterface.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
