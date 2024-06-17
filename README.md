# URL-Shortener
This project is a simple URL shortener that uses the Bitly API to shorten a provided link. Here's a breakdown of the code:

1. **Function `get_link()`**: This function prompts the user to enter a URL, which is then returned as the `LINK` variable.

2. **Function `shortener(LINK, TOKEN)`**: This function takes the `LINK` and `TOKEN` as parameters. It constructs a JSON payload for the Bitly API with the `long_url` key set to the provided `LINK`. The `Authorization` header is set to include the provided `TOKEN`. The function then sends a POST request to the Bitly API to shorten the URL. The response from the API includes the shortened link, which is returned by the function.

3. **Main Code**: The main code gets the user's input for the URL using `get_link()`, then uses `shortener()` to shorten the URL. Finally, it prints the shortened link.

This project demonstrates how to use the Bitly API to shorten URLs programmatically.
