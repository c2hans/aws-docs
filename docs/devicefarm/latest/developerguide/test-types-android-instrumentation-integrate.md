---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-instrumentation-integrate.html
---

# Integrating Android Instrumentation with Device Farm
<a name="test-types-android-instrumentation-integrate"></a>

**Note**
Use the following instructions to integrate Android instrumentation tests with AWS Device Farm. For more information about using instrumentation tests in Device Farm, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md).

## Upload your Android instrumentation tests
<a name="test-types-android-instrumentation-upload"></a>

Use the Device Farm console to upload your tests.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. In the list of projects, choose the project that you want to upload your tests to.
**Tip**
You can use the search bar to filter the project list by name.
To create a project, follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md).

1. Select **Create run**.

1. Under **Select app**, in the **App selection options** section, select **Upload own app**.

1. Browse to and choose your Android app file. The file must be an .apk file.

1. Under **Configure test**, in the **Select test framework** section, choose **Instrumentation**, and then select **Choose File**.

1. Browse to and choose the .apk file that contains your tests.

1. Complete the remaining instructions to select devices and start the run.

## (Optional) Take screenshots in Android instrumentation tests
<a name="test-types-android-instrumentation-screenshots"></a>

You can take screenshots as part of your Android Instrumentation tests.

To take screenshots, call one of the following methods:
+ For Robotium, call the `takeScreenShot` method (for example, `solo.takeScreenShot();`).
+ For Spoon, call the `screenshot` method, for example:

  ```
  Spoon.screenshot(activity, "initial_state");
  /* Normal test code... */
  Spoon.screenshot(activity, "after_login");
  ```

During a test run, Device Farm gets screenshots from the following locations on the devices, if they exist, and then adds them to the test reports:
+ `/sdcard/robotium-screenshots`
+ `/sdcard/test-screenshots`
+ `/sdcard/Download/spoon-screenshots/{{test-class-name}}/{{test-method-name}}`
+ `/data/data/{{application-package-name}}/app_spoon-screenshots/{{test-class-name}}/{{test-method-name}}`
