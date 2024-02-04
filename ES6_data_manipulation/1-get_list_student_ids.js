export default function getListStudentIds(objArr) {
    if (!Array.isArray(objArr)) {
      return [];
    }
  
    return objArr.map((elem) => elem.id);
  }
