---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/troubleshooting-component.html
---

# Detailed component status codes
<a name="troubleshooting-component"></a>

Use the status codes and solutions in these sections to help resolve issues with components when using the Greengrass nucleus version 2.8.0 or later.

Many of the statuses in this topic report additional information in the AWS IoT Greengrass Core logs. These logs are stored on the core device's local file system. There are logs for each individual component. For information on accessing the logs, see [Access file system logs](monitor-logs.md#access-local-logs).

INSTALL\_ERROR
You might get this when an error occurs while running an installation script. The error code is reported in the component log. Check the installation script for errors and deploy your component again.

INSTALL\_CONFIG\_NOT\_VALID
You might get this error when installation of a component couldn't be completed because the `install` section of the recipe isn't valid. Check the installation section of your recipe for errors and try the deployment again.

INSTALL\_IO\_ERROR
You might get this when an I/O error occurred during installation of a component. Check the component error log for details about the error.

INSTALL\_MISSING\_DEFAULT\_RUNWITH
You might get this error when AWS IoT Greengrass can't determine the user or group to use when installing a component. Check to make sure that the `runWith` section of your installation recipe includes a valid user or group.

INSTALL\_TIMEOUT
You might get this error when the installation script did not finish within the configured timeout period. Either increase the `Timeout` period specified in the recipe's `install` section or modify your installation script to finish within the configured timeout.

STARTUP\_ERROR
You might get this when an error occurs while running a startup script. The error code is reported in the component log. Check the installation script for errors and deploy your component again.

STARTUP\_CONFIG\_NOT\_VALID
You might get this error when installation of a component couldn't be completed because the `startup` section of the recipe isn't valid. Check the startup section of your recipe for errors and try the deployment again.

STARTUP\_IO\_ERROR
You might get this when an I/O error occurred during startup of a component. Check the component error log for details about the error.

STARTUP\_MISSING\_DEFAULT\_RUNWITH
You might get this error when AWS IoT Greengrass can't determine the user or group to use when running a component. Check to make sure that the `runWith` section of your startup recipe includes a valid user or group.

STARTUP\_TIMEOUT
You might get this error when the startup script did not finish within the configured timeout period. Either increase the `Timeout` period specified in the recipe's `startup` section or modify your startup script to finish within the configured timeout.

RUN\_ERROR
You might get this when an error occurs while running a component script. The error code is reported in the component log. Check the run script for errors and deploy your component again.

RUN\_MISSING\_DEFAULT\_RUNWITH
You might get this error when AWS IoT Greengrass can't determine the user or group to use when running a component. Check to make sure that the `runWith` section of your run recipe includes a valid user or group.

RUN\_CONFIG\_NOT\_VALID
You might get this error when a component couldn't be run because the `run` section of the recipe isn't valid. Check the run section of your recipe for errors and try the deployment again.

RUN\_IO\_ERROR
You might get this when an I/O error occurred while the component is running. Check the component error log for details about the error.

RUN\_TIMEOUT
You might get this error when the run script did not finish within the configured timeout period. Either increase the `Timeout` period specified in the recipe's `run` section or modify your run script to finish within the configured timeout.

SHUTDOWN\_ERROR
You might get this when an error occurs while shutting down a component script. The error code is reported in the component log. Check the shutdown script for errors and deploy your component again.

SHUTDOWN\_TIMEOUT
You might get this error when the shutdown script did not finish within the configured timeout period. Either increase the `Timeout` period specified in the recipe's `shutdown` section or modify your run script to finish within the configured timeout.

UNINSTALL\_ERROR
You might get this when an error occurs while running the uninstall script during component removal. The error code is reported in the component log. Check the uninstall script for errors. Uninstall failures do not fail the deployment, and the component is still removed from the device.

UNINSTALL\_TIMEOUT
You might get this error when the uninstall script did not finish within the configured timeout period. Either increase the `Timeout` period specified in the recipe's `uninstall` section or modify your uninstall script to finish within the configured timeout. The default timeout is 120 seconds. Uninstall failures do not fail the deployment, and the component is still removed from the device.
