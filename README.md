This is additional info to the original README.md file. 

The code is combined into one script and modified.
The bad request and not found responses are seperated into their own functions to keep things clean:

* The bad_request_response() function is separate from handle_request() and handles bad requests more clearly, without cluttering the main logic.
* The not_found_response() function handles the 404 case, so write_response() doesn't get overloaded with extra logic.
