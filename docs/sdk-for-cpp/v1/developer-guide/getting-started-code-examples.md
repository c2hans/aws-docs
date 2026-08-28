---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/getting-started-code-examples.html
---

# Getting started with the AWS SDK for C\+\+ code examples
<a name="getting-started-code-examples"></a>

## Structure of the code examples
<a name="structure"></a>

The [C\+\+ example folder](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code) on Github contains project folders for each AWS service. Typically, individual .cpp source files in the folders demonstrate a specific functionality or action for that service. For example, for Amazon DynamoDB, *getting* an item from the database and *uploading* an item to the database are two different types of action, so there is a separate file for each in the DynamoDB folder: `get_item.cpp` and `put_item.cpp`. Each .cpp file contains a `main()` function as an entrypoint to a standalone executable. The project executables are generated in a folder designated by your build system, and there is one executable file corresponding to each example source file. The file name of the executable follows the conventions of the platform such as `{name}.exe` or just `{name}` and any custom prefix `CMakeLists.txt` applies such as `run_`.

**To run an example functionality**

1. Download the desired code example from the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code) on GitHub.

1. Open a .cpp file to explore its `main()` function and any called methods.

1. Build the project, as demonstrated with the starter example in [Getting started using the AWS SDK for C\+\+](getting-started.md). Note that building the project generates each executable for every source file in the project.

1. Run the executable for the selected functionality.
   + In a command prompt, run that program using the executable based on the name of the `*.cpp` file.
   + If you are working within an IDE, choose the `.cpp` file of the functionality you want to demonstrate and select it as the startup option (or startup object).

### Unit tests
<a name="unittest"></a>

Tests for examples are written using the GoogleTest framework. To learn more, see [GoogleTest Primer](https://google.github.io/googletest/primer.html) on the GoogleTest website.

The unit tests for each example are in a `tests` subfolder containing its own `CMakeLists.txt` file. For each example source file there is a corresponding test file named `gtest_{{<source file>}}`. The test executable for the subfolder is named `{{<AWS service>}}_gtests`.

### CMakeLists.txt file
<a name="CMakeLists"></a>

The folder for each service contains a file named `CMakeLists.txt` file. Many of these files contain a construct similar to the following:

```
foreach(EXAMPLE IN LISTS EXAMPLES)
         add_executable(${EXAMPLE} ${EXAMPLE}.cpp)
         target_link_libraries(${EXAMPLE} aws-cpp-sdk-email aws-cpp-sdk-core)
endforeach()
```

 For each .cpp file in the folder, the `CMakeLists.txt` file builds an executable (cmake: `add_executable`) with a name based on the name of the source code file without the file extension.

## Building and Debugging Code Examples in Visual Studio
<a name="buildingOnVisualStudio"></a>

**Building and running the Amazon S3 code example**

1. Obtain the Amazon S3 example source code. This procedure uses the [Amazon S3 code examples using the AWS SDK for C\+\+](examples-s3.md) code example to get up and running using Visual Studio.

1. In Windows Explorer, navigate to the `s3` folder (e.g. `\aws-doc-sdk-examples\cpp\example_code\s3`).

1. Right click on the `s3` example folder and choose **Open with Visual Studio**.  Visual Studio for CMake projects don’t have a 'project' file, rather, it is the whole folder.

1. In the **Configuration Selector** dropdown in the top menu of Visual Studio, ensure that the selected configuration matches the build type that you selected when building the SDK from source.  E.g. a **Debug** configuration should be selected if you built from source using debug (`-DCMAKE_BUILD_TYPE=Debug` in the CMake command line from the SDK installation instructions).

1. Open file `CMakeLists.txt`.

1. Click **Save**. Every time you click **Save** on the `CMakeLists.txt` file, Visual Studio refreshes the CMake-generated files.  If you have your **Output** tab displayed, you can see the resulting log messages from this generation.
   + There is a drop-down box within the **Output** tab that says: "**Show output from:**" and **CMake** should be the option selected by default.
   + Last message output should say "**CMake generation finished.**"
   + If last message is not this, then the CMake file has issues. Do not proceed to further steps until this is resolved.  See [Troubleshooting AWS SDK for C\+\+ build issues](troubleshooting-cmake.md).
   + Note that the CMake cache is used by CMake for speed. If you are working through CMake issues, you want to ensure a ‘clean slate’ so that the error messages you are given is actually reflective of your most recent changes.  In the Solution Explorer, right-click on `CMakeLists.txt` and choose **CMake Cache**, then choose **Delete Cache**. Do this frequently when working progressively through CMake issues.

1. To build and run examples from within Visual Studio, Visual Studio places executables in a different folder structure than the command line. To run the code, the SDK executables must be copied to the right place.  Find the “`TODO`” line of the CMakeLists file (\~line 40) and choose the one commented for use in Visual Studio. Visual Studio does not use a subfolder dedicated to the build type so this is not included.  Switch the commented-out line in the `CMakeLists.txt` file for Visual Studio use.

1. Delete the CMake cache (as described above), click in the `CMakeLists.txt` file to select/activate the tab, and choose **Save** on the `CMakeLists.txt` file again to initiate the CMake build files generation.

1. Open the source file of the ‘program’ you wish to run.
   + For example, open `list_buckets.cpp`.
   + The Amazon S3 example folder is coded so that each showcased ‘feature’ of Amazon S3 is demonstrated in a dedicated executable for just that feature.  E.g. `list_buckets.cpp` will become an executable that only demonstrates the listing of buckets.

1. In the top menu, choose **Build**, then choose **Build All**.
   + The **Output** tab’s **Show output from** should reflect the selection of **Build**, and show all the building and linking messages.
   + The last output should be: "**Build All succeeded.**"
   + Now executables for each of the individual source files are generated.  You can confirm this by looking in the build output directory (e.g. `\aws-doc-sdk-examples\cpp\example_code\s3\out\build\x64-Debug`).
   + Note that the executables are prefixed with “run\_” because the `CMakeLists.txt` file dictates this.

1. In the top menu, there is a **green arrow** and a **drop-down selector** for **Debug Target**.  Choose `run_list_buckets.exe`.

1. Click the **green arrow run button** to **Select Startup Item**.

1. A Visual Studio Debug Console window will open and display the output of the code.

1. Press a key to close the window, or manually close the window, to terminate the program.  You can also set breakpoints in the code and when you click run again the breakpoints will be hit.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
