"""
@author: Nicolò Morini 

"""
import sys, signal
import http.server
import socketserver

def check_parameters ():
    if len(sys.argv) != 3:
        print (len(sys.argv))
        print("Il comando non è corretto. Usa il seguente formato: Py_webserver.py indirizzo_ip_del_server_web porta_del_server")
        sys.exit(0)

def main():
    if sys.argv[2:]:
      server_port = int(sys.argv[2])
    else:
      server_port = 8080
      
    server_ip_address = sys.argv[1]

    server = socketserver.ThreadingTCPServer((server_ip_address, server_port), http.server.SimpleHTTPRequestHandler)
    
    server.daemon_threads = True
    server.allow_reuse_address = True 
    
    def signal_handler(signal, frame):
        print( 'Exiting http server (Ctrl+C pressed)')
        try:
          if( server ):
            server.server_close()
        finally:
          sys.exit(0)
          
    signal.signal(signal.SIGINT, signal_handler)

    try:
      while True:
        print("Server HTTP in ascolto su:")
        print("IP:", server_ip_address)
        print("PORT:", server_port)
        print("Per terminare il server premere il comando (Ctrl + C)")
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
  
    check_parameters()
    main()