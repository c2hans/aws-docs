---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/detect-network-latency.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

# Detecting network latency
<a name="detect-network-latency"></a>

If your WorkSpaces Thin Client device is lagging in either performance or display, it may be experiencing network latency. Network latency is measured in milliseconds (ms). If a WorkSpaces Thin Client device has a network latency over 150 ms, a notification will appear.

![Amazon WorkSpaces sign-in page with high latency notification alert.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/network_latency_notification.png)

When this occurs, you can check your network connection for any possible issues.

1. Go to **Settings**, **Network**.

1. Select **Check your network connection**.
![Network settings interface with options to view, connect to, and add networks.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/check-network.png)

1. Verify the following have green checks:
   + Device has a valid IP address
   + Streaming host is reachable
   + Latency to streaming host is under 150 milliseconds (ms).
![Network check results showing WiFi connection, valid IP address, and streaming host latency.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/checklist-network.png)

If an issue appears within that checklist, contact your administrator.
