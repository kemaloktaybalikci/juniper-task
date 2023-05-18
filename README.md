# juniper-task
This is an assignment repository prepared by me for Juniper Networks.

## Task Description
According to the task requirements, a function needs to be written to return the minimum subnet spanning of the given IPv4 addresses. It is requested to consider memory and CPU efficiency while implementing the function.

## Project Content
The project consists of 2 files. The 'utils.py' file contains the function required for the task. I tried to write the test scenarios in the 'test.py' file.
I used Python 3.8 version.

## Project Run
You can run the project with the command 'python test.py'. Alternatively, you can call the 'find_common_subnets(ip_addresses)' command under 'utils.py' yourself. The function will return a tuple value of 'result_state, result'.

## Task Background
I completed the project content in approximately one day. I am aware that the task is expected to take about 1 hour, but due to my lack of knowledge in the networking field, the research and development process took a bit longer. I must admit that I learned a lot during this process, even though I didn't even know terms like network, subnet, mask.

I worked with the 'ipaddresses' and 'netaddr' libraries and read their documentation. Unfortunately, I couldn't achieve the desired results using functions like 'subnet_of', 'supernet', 'cidr_merge' with these libraries, so I followed a path where I could come up with my own solution.

In the task, I chose a path that progresses by splitting string values, but later in my research, I realized that taking the 'longest_common_prefix' value in the 'binary' format rather than the 'string' format would be more efficient, but I couldn't implement this change in order not to be even more delayed.

In the function inside 'utils.py', I tried to gain efficiency in terms of memory and CPU as much as possible. If the IP list has a large number of elements, the early escape could have been applied for the first IP block. These are my observations and details that I have noticed for now. Remember that your feedback is important to me. Thank you for your attention.
