from Database import conectar

def agregar_libro(titulo, autor, genero, estado):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor, genero, estado) VALUES (?, ?, ?, ?)",
                   (titulo, autor, genero, estado))
    conexion.commit()
    conexion.close()

def actualizar_libro(id_libro, campo, nuevo_valor):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(f"UPDATE libros SET {campo} = ? WHERE id = ?", (nuevo_valor, id_libro))
    conexion.commit()
    conexion.close()

def eliminar_libro(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conexion.commit()
    conexion.close()

def ver_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conexion.close()
    return libros

def buscar_libros(clave, valor):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM libros WHERE {clave} LIKE ?", ('%' + valor + '%',))
    resultados = cursor.fetchall()
    conexion.close()
    return resultados
