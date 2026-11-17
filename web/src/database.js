import initSqlJs from 'sql.js';
import wasm from 'sql.js/dist/sql-wasm.wasm?url';
export async function createDatabase(){
 const SQL=await initSqlJs({locateFile:()=>wasm});const db=new SQL.Database();
 db.run('CREATE TABLE queries(id INTEGER PRIMARY KEY, engine TEXT, algorithm TEXT, latency_ms REAL, recall REAL, source TEXT NOT NULL)');
 let seed=42;const random=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296};
 const engines=['Faiss','pgvector','OpenSearch'];const algorithms=['HNSW','IVF-PQ'];
 const stmt=db.prepare('INSERT INTO queries VALUES(?,?,?,?,?,?)');db.run('BEGIN');
 for(let id=1;id<=50000;id++){const engine=engines[(id-1)%3],algorithm=algorithms[id%2];stmt.run([id,engine,algorithm,Math.round((.2+random()*8)*1000)/1000,Math.round((.5+random()*.5)*100)/100,'mock']);}
 stmt.free();db.run('COMMIT');db.run('CREATE INDEX query_engine ON queries(engine)');return db;
}
export function rows(db,sql,params=[]){const q=db.prepare(sql);q.bind(params);const out=[];while(q.step())out.push(q.getAsObject());q.free();return out;}
