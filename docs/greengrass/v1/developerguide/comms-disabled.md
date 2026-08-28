---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/comms-disabled.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Test communications (device syncs disabled)
<a name="comms-disabled"></a>

1. <a name="ping-device"></a>Make sure that your computer and the AWS IoT Greengrass core device are connected to the internet using the same network.

   1. On the AWS IoT Greengrass core device, run the following command to find its IP address.

      ```
      hostname -I
      ```

   1. On your computer, run the following command using the IP address of the core. You can use Ctrl \+ C to stop the **ping** command.

      ```
      ping {{IP-address}}
      ```

      Output similar to the following indicates successful communication between the computer and the AWS IoT Greengrass core device (0% packet loss):
![Successful ping command output.](http://docs.aws.amazon.com/greengrass/v1/developerguide/images/gg-get-started-075.5.png)
**Note**
If you're unable to ping an EC2 instance that's running AWS IoT Greengrass, make sure that the inbound security group rules for the instance allow ICMP traffic for [Echo request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html#sg-rules-ping) messages. For more information, see [ Adding rules to a security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#adding-security-group-rule) in the *Amazon EC2 User Guide*.
On Windows host computers, in the Windows Firewall with Advanced Security app, you might also need to enable an inbound rule that allows inbound echo requests (for example, **File and Printer Sharing (Echo Request - ICMPv4-In)**), or create one.

1. Get your AWS IoT endpoint.

   1. <a name="iot-settings"></a>From the [AWS IoT console](https://console.aws.amazon.com/iot/) navigation pane, choose **Settings**.

   1. <a name="iot-settings-endpoint"></a>Under **Device data endpoint**, make a note of the value of **Endpoint**. You use this value to replace the {{AWS\_IOT\_ENDPOINT}} placeholder in the commands in the following steps.
**Note**
Make sure that your [endpoints correspond to your certificate type](gg-core.md#certificate-endpoints).

1. <a name="repeated-step"></a>On your computer (not the AWS IoT Greengrass core device), open two [command-line](https://en.wikipedia.org/wiki/Command-line_interface) (terminal or command prompt) windows. One window represents the GG\_Switch client device and the other represents the GG\_TrafficLight client device.

   1. <a name="run-switch-device"></a>From the GG\_Switch client device window, run the following commands.
      + Replace {{path-to-certs-folder}} with the path to the folder that contains the certificates, keys, and Python files.
      + Replace {{AWS\_IOT\_ENDPOINT}} with your endpoint.
      + Replace the two {{switchCertId}} instances with the certificate ID in the file name for your GG\_Switch client device.

      ```
      cd {{path-to-certs-folder}}
      python lightController.py --endpoint {{AWS_IOT_ENDPOINT}} --rootCA AmazonRootCA1.pem --cert {{switchCertId}}-certificate.pem.crt --key {{switchCertId}}-private.pem.key --thingName GG_TrafficLight --clientId GG_Switch
      ```

   1. <a name="run-trafficlight-device"></a>From the GG\_TrafficLight client device window, run the following commands.
      + Replace {{path-to-certs-folder}} with the path to the folder that contains the certificates, keys, and Python files.
      + Replace {{AWS\_IOT\_ENDPOINT}} with your endpoint.
      + Replace the two {{lightCertId}} instances with the certificate ID in the file name for your GG\_TrafficLight client device.

      ```
      cd {{path-to-certs-folder}}
      python trafficLight.py --endpoint {{AWS_IOT_ENDPOINT}} --rootCA AmazonRootCA1.pem --cert {{lightCertId}}-certificate.pem.crt --key {{lightCertId}}-private.pem.key --thingName GG_TrafficLight --clientId GG_TrafficLight
      ```

      Every 20 seconds, the switch updates the shadow state to G, Y, and R, and the light displays its new state, as shown next.

      GG\_Switch output:
![Screenshot of the output associated with GG_Switch.](http://docs.aws.amazon.com/greengrass/v1/developerguide/images/gg-get-started-083.png)

      GG\_TrafficLight output:
![Screenshot of the output associated with GG_TrafficLight.](http://docs.aws.amazon.com/greengrass/v1/developerguide/images/gg-get-started-084.png)

   When executed for the first time, each client device script runs the AWS IoT Greengrass discovery service to connect to the AWS IoT Greengrass core (through the internet). After a client device has discovered and successfully connected to the AWS IoT Greengrass core, future operations can be executed locally.
**Note**
<a name="check-connection-info"></a> The `lightController.py` and `trafficLight.py` scripts store connection information in the `groupCA` folder, which is created in the same folder as the scripts. If you receive connection errors, make sure that the IP address in the `ggc-host` file matches the IP address endpoint for your core.

1. In the AWS IoT console, choose your AWS IoT Greengrass group, choose the **Client devices** tab, and then choose **GG\_TrafficLight** to open the client device's AWS IoT thing details page.

1. Choose the **Device Shadows** tab. After the GG\_Switch changes states, there should not be any updates to this shadow. That's because the GG\_TrafficLight is set to **Disable shadow sync with cloud**.

1. Press Ctrl \+ C in the GG\_Switch (`lightController.py`) client device window. You should see that the GG\_TrafficLight (`trafficLight.py`) window stops receiving state change messages.

   Keep these windows open so you can run the commands in the next section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
