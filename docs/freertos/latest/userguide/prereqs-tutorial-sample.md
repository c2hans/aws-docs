---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/prereqs-tutorial-sample.html
---

# Set up the prerequisites for the sample test suite
<a name="prereqs-tutorial-sample"></a>

To complete this tutorial, you need the following:
+

  **Host computer requirements**
  + Latest version of AWS IoT Device Tester
  + [Python](https://docs.python.org/3/) 3.7 or later

    To check the version of Python installed on your computer, run the following command:

    ```
    python3 --version
    ```

    On Windows, if using this command returns an error, then use `python --version` instead. If the returned version number is 3.7 or greater, then run the following command in a Powershell terminal to set `python3` as an alias for your `python` command.

    ```
    Set-Alias -Name "python3" -Value "python"
    ```

    If no version information is returned or if the version number is less than 3.7, follow the instructions in [Downloading Python](https://wiki.python.org/moin/BeginnersGuide/Download) to install Python 3.7\+. For more information, see the [Python documentation](https://docs.python.org/3/).
  + [urllib3](https://urllib3.readthedocs.io/en/latest/)

    To verify that `urllib3` is installed correctly, run the following command:

    ```
    python3 -c 'import urllib3'
    ```

    If `urllib3` is not installed, run the following command to install it:

    ```
    python3 -m pip install urllib3
    ```
+

  **Device requirements**
  + A device with a Linux operating system and a network connection to the same network as your host computer.

    We recommend that you use a [Raspberry Pi](https://www.raspberrypi.org/) with Raspberry Pi OS. Make sure you set up [SSH](https://www.raspberrypi.com/documentation/computers/remote-access.html) on your Raspberry Pi to remotely connect to it.
