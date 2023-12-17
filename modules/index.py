import sqlite3

conn=sqlite3.connect("database.db")
cursor=conn.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            email TEXT
        )
    """
)

conn.commit()


#Crear usuario -> C
def crear_usuario(nombre: str, email: str) -> str:
    try:
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES(?, ?)", (nombre, email))
        conn.commit()
        return "Usuario creado exitosamente"
    except:
        return "Error al crear el usuario"


#Leer registros -> R
def obtener_usuarios() -> list:
    cursor.execute("SELECT id, nombre, email FROM usuarios")
    usuarios=cursor.fetchall()
    lista_usuario=[]
    
    for usuario in usuarios:
        lista_usuario.append(usuario)
    
    return lista_usuario

#Actualizar usuario por id -> U
def actualizar_usuario(id:int, nombre:str, email:str) -> str:
    cursor.execute("UPDATE usuarios SET nombre=?, email=? WHERE id = ?", (nombre, email, id))
    conn.commit()
    return f"Usuario actualizado"

#Eliminar usuario por id -> D
def eliminar_usuario(id: int) -> str:
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    return "Usuario eliminado"

#Leer registro por id
def obtener_usuario(id:int) -> str:
    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = ?", (id,))
    usuario=cursor.fetchone()
    
    if usuario != None:
        return usuario
    else:
        return "Usuario no encontrado"
    
# print(crear_usuario("Nicolas","lugonesnicolas@example.com"))
# print(crear_usuario("Elias","lugoneselias@example.com"))
# print(crear_usuario("Nahir","gramajonahir@example.com"))
# print(obtener_usuarios())
# print(actualizar_usuario(3,"Ingrid","gramajoingrid@example.com"))
# print(obtener_usuario(1))
# print(eliminar_usuario(3))