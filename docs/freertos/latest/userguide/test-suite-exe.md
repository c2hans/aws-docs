---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/test-suite-exe.html
---

# Create the test case executable
<a name="test-suite-exe"></a>

Test case executables contain the test logic that you want to run. A test suite can contain multiple test case executables. For this tutorial, you will create only one test case executable.

1. Create the test suite file.

   In the `MyTestSuite_1.0.0/suite/myTestGroup/myTestCase` folder, create a `myTestCase.py` file with the following content:

   ```
   from idt_client import *

   def main():
       # Use the client SDK to communicate with IDT
       client = Client()

   if __name__ == "__main__":
       main()
   ```

1. Use client SDK functions to add the following test logic to your `myTestCase.py` file:

   1. Run an SSH command on the device under test.

      ```
      from idt_client import *

      def main():
          # Use the client SDK to communicate with IDT
          client = Client()

          {{# Create an execute on device request
          exec_req = ExecuteOnDeviceRequest(ExecuteOnDeviceCommand("echo 'hello world'"))

          # Run the command
          exec_resp = client.execute_on_device(exec_req)

          # Print the standard output
          print(exec_resp.stdout)}}

      if __name__ == "__main__":
          main()
      ```

   1. Send the test result to IDT.

      ```
      from idt_client import *

      def main():
          # Use the client SDK to communicate with IDT
          client = Client()

          # Create an execute on device request
          exec_req = ExecuteOnDeviceRequest(ExecuteOnDeviceCommand("echo 'hello world'"))

          # Run the command
          exec_resp = client.execute_on_device(exec_req)

          # Print the standard output
          print(exec_resp.stdout)

          {{# Create a send result request
          sr_req = SendResultRequest(TestResult(passed=True))

          # Send the result
          client.send_result(sr_req)}}

      if __name__ == "__main__":
          main()
      ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
