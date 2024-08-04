import sqlite3


def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    """Create a table for storing film equipment details"""
    try:
        sql_create_equipment_table = """CREATE TABLE IF NOT EXISTS equipment (
                                            equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            name TEXT NOT NULL,
                                            type TEXT NOT NULL,
                                            brand TEXT NOT NULL,
                                            price REAL NOT NULL
                                        );"""
        print("Creating equipment table...")
        conn.execute(sql_create_equipment_table)
    except sqlite3.Error as e:
        print(e)


def insert_equipment(conn, equipment):
    """Insert new equipment into the equipment table"""
    sql = '''INSERT INTO equipment(name, type, brand, price)
             VALUES(?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, equipment)
    conn.commit()
    return cur.lastrowid


def update_equipment(conn, equipment):
    """Update an equipment's details"""
    sql = '''UPDATE equipment
             SET name = ?,
                 type = ?,
                 brand = ?,
                 price = ?
             WHERE equipment_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, equipment)
    conn.commit()


def fetch_equipment(conn):
    """Fetch all equipment details"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM equipment")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# Example usage:
if __name__ == '__main__':
    database = "data/film_equipment.db"

    # Create a database connection
    conn = create_connection(database)

    with conn:
        # Create equipment table
        create_table(conn)

        # Insert new equipment
        film_equipments = [
            ('Tripod', 'Support', 'Manfrotto', 250.00),
            ('Camera', 'Digital', 'Canon', 1500.00),
            ('Lens', 'Prime', 'Nikon', 900.00),
            ('Light', 'LED', 'Aputure', 300.00),
            ('Microphone', 'Shotgun', 'Rode', 200.00),
            ('Monitor', 'Field', 'Atomos', 400.00),
            ('Gimbal', 'Stabilizer', 'DJI', 450.00),
            ('Slider', 'Track', 'Rhino', 500.00),
            ('Recorder', 'Audio', 'Zoom', 250.00),
            ('Softbox', 'Lighting', 'Godox', 120.00),
            ('Backdrop', 'Support', 'Impact', 80.00),
            ('Drone', 'Aerial', 'DJI', 1200.00),
            ('Battery', 'Rechargeable', 'Sony', 60.00),
            ('Charger', 'Battery', 'Sony', 40.00),
            ('Filter', 'ND', 'Tiffen', 100.00),
            ('Bag', 'Camera', 'Lowepro', 150.00),
            ('Card', 'Memory', 'SanDisk', 80.00),
            ('Reader', 'Card', 'Lexar', 30.00),
            ('Stand', 'Light', 'Neewer', 50.00),
            ('Headphones', 'Monitoring', 'Audio-Technica', 100.00),
            ('Boom Pole', 'Audio', 'K-Tek', 200.00),
            ('Reflector', 'Light', 'Westcott', 40.00),
            ('Tripod Head', 'Fluid', 'Manfrotto', 150.00),
            ('Clamp', 'Mount', 'Impact', 25.00),
            ('Rig', 'Shoulder', 'Tilta', 700.00),
            ('Matte Box', 'Lens', 'SmallRig', 300.00),
            ('Follow Focus', 'Lens Control', 'Tilta', 350.00),
            ('Monitor Mount', 'Support', 'SmallRig', 80.00),
            ('Lens Cap', 'Protection', 'Canon', 10.00),
            ('Lens Hood', 'Shade', 'Canon', 30.00),
            ('Lens Cleaner', 'Accessory', 'Zeiss', 15.00),
            ('Memory Case', 'Storage', 'Pelican', 25.00),
            ('Rain Cover', 'Protection', 'Think Tank', 50.00),
            ('Gaffer Tape', 'Adhesive', 'Pro Tapes', 20.00),
            ('Light Stand', 'Support', 'Avenger', 100.00),
            ('C-Stand', 'Support', 'Matthews', 180.00),
            ('Sandbag', 'Stabilizer', 'Impact', 20.00),
            ('Diffuser', 'Light', 'Rosco', 60.00),
            ('Grid', 'Light Modifier', 'Chimera', 100.00),
            ('Softbox', 'Lighting', 'Aputure', 150.00),
            ('V-Mount Battery', 'Power', 'IDX', 300.00),
            ('V-Mount Charger', 'Power', 'IDX', 200.00),
            ('Lav Mic', 'Audio', 'Sennheiser', 250.00),
            ('Wireless System', 'Audio', 'Sennheiser', 500.00),
            ('Shock Mount', 'Audio', 'Rycote', 100.00),
            ('Windshield', 'Audio', 'Rycote', 150.00),
            ('Light Panel', 'LED', 'Luxli', 200.00),
            ('Light Dome', 'Lighting', 'Aputure', 200.00),
            ('Bounce Board', 'Light', 'Lastolite', 70.00),
            ('Grip Head', 'Support', 'Avenger', 40.00),
            ('Magic Arm', 'Mount', 'Manfrotto', 130.00),
            ('Slider Motor', 'Motor', 'Rhino', 700.00),
            ('Dolly', 'Camera', 'Proaim', 1000.00),
            ('Tripod Plate', 'Mount', 'Manfrotto', 50.00),
            ('Cage', 'Camera', 'SmallRig', 150.00),
            ('Follow Focus', 'Lens Control', 'Tilta', 350.00),
            ('Monitor Hood', 'Accessory', 'SmallRig', 30.00),
            ('Wireless Video', 'Transmission', 'Teradek', 1500.00),
            ('Eyecup', 'Viewfinder', 'Hoodman', 20.00)
        ]
        for film_equipment in film_equipments:
            insert_equipment(conn, film_equipment)


        # Update equipment
        updated_equipment = ('Updated Camera', 'Video', 'Canon', 1300.00, 1)
        update_equipment(conn, updated_equipment)

        # Fetch all equipment details
        fetch_equipment(conn)

    # Close the connection
    if conn:
        conn.close()

