alias hexdecode='python -c "import sys; print(\"\".join([chr(int(\"0x{}{}\".format(sys.argv[1][i], sys.argv[1][i+1]), 16)) for i in range(0, len(sys.argv[1]), 2)]))"'
