from flask import Flask, render_template, request

app = Flask(__name__)
import sqlite3


# main route 
@app.route("/")
def index():
    #initiate DB connection
    conn=sqlite3.connect('../sensorsData.db')
    curs=conn.cursor()

    #retrieve data from DB
    for row in curs.execute("SELECT * FROM MLX_data ORDER BY timestamp DESC LIMIT 1"):
        timestamp = str(row[0])
        ds18b20_object = row[1]
        mlx_ambient = row[2]  
        mlx_object = row[3]    
    
    conn.close()
        
    templateData = {
        'time': timestamp,
        'ds_temp': ds18b20_object,
        'mlx_amb': mlx_ambient,
        'mlx_obj' : mlx_object
    }
    return render_template('index.html', **templateData)
    
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=55555, debug=False)
