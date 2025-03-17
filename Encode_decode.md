# Simple Message Encoder/Decoder

This Python script allows you to encode or decode a message using a simple custom algorithm.

## How it Works

The script takes a message as input and then asks the user whether they want to encode or decode it.

**Encoding:**

If you choose to encode (by entering `1`), the script will process each word in the message as follows:

* **For words with 3 or more letters:**
    * It adds three random lowercase letters at the beginning of the word.
    * It moves the first letter of the original word to the end.
    * It adds another three random lowercase letters at the end of the modified word.
* **For words with less than 3 letters:**
    * It simply reverses the word.

**Decoding:**

If you choose to decode (by entering `0`), the script will process each word in the encoded message as follows:

* **For words with 3 or more letters:**
    * It removes the first three letters.
    * It removes the last three letters.
    * It moves the last letter of the remaining string to the beginning.
* **For words with less than 3 letters:**
    * It simply reverses the word.

## How to Use

1.  **Save the code:** Save the provided Python code as a `.py` file (e.g., `encoder_decoder.py`).
2.  **Run the script:** Open a terminal or command prompt and navigate to the directory where you saved the file. Then, run the script using the command: `python encoder_decoder.py`
3.  **Enter the message:** The script will prompt you to "Enter message". Type your message and press Enter.
4.  **Choose encoding or decoding:** The script will ask "1 for Coding or 0 for Decoding". Enter `1` to encode or `0` to decode and press Enter.
5.  **View the result:** The script will print `True` if you chose encoding and `False` if you chose decoding, followed by the encoded or decoded message.

## Example

**Encoding:**


Enter message: This is a secret message
1 for Coding or 0 for Decoding: 1
True
abcishTdef ghi sji akl ecretsbm nessagexyz

**Decoding (using the output from the encoding example):**


Enter message: abcishTdef ghi sji akl ecretsbm nessagexyz
1 for Coding or 0 for Decoding: 0
False
This is a secret message

## Note

This is a very basic encoding/decoding algorithm and should not be used for any serious security purposes. It's primarily for educational or recreational use.

