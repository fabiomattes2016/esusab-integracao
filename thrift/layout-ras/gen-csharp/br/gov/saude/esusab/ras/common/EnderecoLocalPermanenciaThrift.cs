/**
 * Autogenerated by Thrift Compiler (0.9.3)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.IO;
using Thrift;
using Thrift.Collections;
using System.Runtime.Serialization;
using Thrift.Protocol;
using Thrift.Transport;

namespace br.gov.saude.esusab.ras.common
{

  #if !SILVERLIGHT
  [Serializable]
  #endif
  public partial class EnderecoLocalPermanenciaThrift : TBase
  {
    private string _bairro;
    private string _cep;
    private string _codigoIbgeMunicipio;
    private string _complemento;
    private string _nomeLogradouro;
    private string _numero;
    private string _numeroDneUf;
    private string _telefoneContato;
    private string _telefoneResidencia;
    private string _tipoLogradouroNumeroDne;
    private bool _stSemNumero;
    private string _pontoReferencia;
    private string _microArea;
    private bool _stForaArea;

    public string Bairro
    {
      get
      {
        return _bairro;
      }
      set
      {
        __isset.bairro = true;
        this._bairro = value;
      }
    }

    public string Cep
    {
      get
      {
        return _cep;
      }
      set
      {
        __isset.cep = true;
        this._cep = value;
      }
    }

    public string CodigoIbgeMunicipio
    {
      get
      {
        return _codigoIbgeMunicipio;
      }
      set
      {
        __isset.codigoIbgeMunicipio = true;
        this._codigoIbgeMunicipio = value;
      }
    }

    public string Complemento
    {
      get
      {
        return _complemento;
      }
      set
      {
        __isset.complemento = true;
        this._complemento = value;
      }
    }

    public string NomeLogradouro
    {
      get
      {
        return _nomeLogradouro;
      }
      set
      {
        __isset.nomeLogradouro = true;
        this._nomeLogradouro = value;
      }
    }

    public string Numero
    {
      get
      {
        return _numero;
      }
      set
      {
        __isset.numero = true;
        this._numero = value;
      }
    }

    public string NumeroDneUf
    {
      get
      {
        return _numeroDneUf;
      }
      set
      {
        __isset.numeroDneUf = true;
        this._numeroDneUf = value;
      }
    }

    public string TelefoneContato
    {
      get
      {
        return _telefoneContato;
      }
      set
      {
        __isset.telefoneContato = true;
        this._telefoneContato = value;
      }
    }

    public string TelefoneResidencia
    {
      get
      {
        return _telefoneResidencia;
      }
      set
      {
        __isset.telefoneResidencia = true;
        this._telefoneResidencia = value;
      }
    }

    public string TipoLogradouroNumeroDne
    {
      get
      {
        return _tipoLogradouroNumeroDne;
      }
      set
      {
        __isset.tipoLogradouroNumeroDne = true;
        this._tipoLogradouroNumeroDne = value;
      }
    }

    public bool StSemNumero
    {
      get
      {
        return _stSemNumero;
      }
      set
      {
        __isset.stSemNumero = true;
        this._stSemNumero = value;
      }
    }

    public string PontoReferencia
    {
      get
      {
        return _pontoReferencia;
      }
      set
      {
        __isset.pontoReferencia = true;
        this._pontoReferencia = value;
      }
    }

    public string MicroArea
    {
      get
      {
        return _microArea;
      }
      set
      {
        __isset.microArea = true;
        this._microArea = value;
      }
    }

    public bool StForaArea
    {
      get
      {
        return _stForaArea;
      }
      set
      {
        __isset.stForaArea = true;
        this._stForaArea = value;
      }
    }


    public Isset __isset;
    #if !SILVERLIGHT
    [Serializable]
    #endif
    public struct Isset {
      public bool bairro;
      public bool cep;
      public bool codigoIbgeMunicipio;
      public bool complemento;
      public bool nomeLogradouro;
      public bool numero;
      public bool numeroDneUf;
      public bool telefoneContato;
      public bool telefoneResidencia;
      public bool tipoLogradouroNumeroDne;
      public bool stSemNumero;
      public bool pontoReferencia;
      public bool microArea;
      public bool stForaArea;
    }

    public EnderecoLocalPermanenciaThrift() {
    }

    public void Read (TProtocol iprot)
    {
      iprot.IncrementRecursionDepth();
      try
      {
        TField field;
        iprot.ReadStructBegin();
        while (true)
        {
          field = iprot.ReadFieldBegin();
          if (field.Type == TType.Stop) { 
            break;
          }
          switch (field.ID)
          {
            case 1:
              if (field.Type == TType.String) {
                Bairro = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 2:
              if (field.Type == TType.String) {
                Cep = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 3:
              if (field.Type == TType.String) {
                CodigoIbgeMunicipio = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 4:
              if (field.Type == TType.String) {
                Complemento = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 5:
              if (field.Type == TType.String) {
                NomeLogradouro = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 6:
              if (field.Type == TType.String) {
                Numero = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 7:
              if (field.Type == TType.String) {
                NumeroDneUf = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 8:
              if (field.Type == TType.String) {
                TelefoneContato = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 9:
              if (field.Type == TType.String) {
                TelefoneResidencia = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 10:
              if (field.Type == TType.String) {
                TipoLogradouroNumeroDne = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 11:
              if (field.Type == TType.Bool) {
                StSemNumero = iprot.ReadBool();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 12:
              if (field.Type == TType.String) {
                PontoReferencia = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 13:
              if (field.Type == TType.String) {
                MicroArea = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 14:
              if (field.Type == TType.Bool) {
                StForaArea = iprot.ReadBool();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            default: 
              TProtocolUtil.Skip(iprot, field.Type);
              break;
          }
          iprot.ReadFieldEnd();
        }
        iprot.ReadStructEnd();
      }
      finally
      {
        iprot.DecrementRecursionDepth();
      }
    }

    public void Write(TProtocol oprot) {
      oprot.IncrementRecursionDepth();
      try
      {
        TStruct struc = new TStruct("EnderecoLocalPermanenciaThrift");
        oprot.WriteStructBegin(struc);
        TField field = new TField();
        if (Bairro != null && __isset.bairro) {
          field.Name = "bairro";
          field.Type = TType.String;
          field.ID = 1;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(Bairro);
          oprot.WriteFieldEnd();
        }
        if (Cep != null && __isset.cep) {
          field.Name = "cep";
          field.Type = TType.String;
          field.ID = 2;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(Cep);
          oprot.WriteFieldEnd();
        }
        if (CodigoIbgeMunicipio != null && __isset.codigoIbgeMunicipio) {
          field.Name = "codigoIbgeMunicipio";
          field.Type = TType.String;
          field.ID = 3;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(CodigoIbgeMunicipio);
          oprot.WriteFieldEnd();
        }
        if (Complemento != null && __isset.complemento) {
          field.Name = "complemento";
          field.Type = TType.String;
          field.ID = 4;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(Complemento);
          oprot.WriteFieldEnd();
        }
        if (NomeLogradouro != null && __isset.nomeLogradouro) {
          field.Name = "nomeLogradouro";
          field.Type = TType.String;
          field.ID = 5;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(NomeLogradouro);
          oprot.WriteFieldEnd();
        }
        if (Numero != null && __isset.numero) {
          field.Name = "numero";
          field.Type = TType.String;
          field.ID = 6;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(Numero);
          oprot.WriteFieldEnd();
        }
        if (NumeroDneUf != null && __isset.numeroDneUf) {
          field.Name = "numeroDneUf";
          field.Type = TType.String;
          field.ID = 7;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(NumeroDneUf);
          oprot.WriteFieldEnd();
        }
        if (TelefoneContato != null && __isset.telefoneContato) {
          field.Name = "telefoneContato";
          field.Type = TType.String;
          field.ID = 8;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(TelefoneContato);
          oprot.WriteFieldEnd();
        }
        if (TelefoneResidencia != null && __isset.telefoneResidencia) {
          field.Name = "telefoneResidencia";
          field.Type = TType.String;
          field.ID = 9;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(TelefoneResidencia);
          oprot.WriteFieldEnd();
        }
        if (TipoLogradouroNumeroDne != null && __isset.tipoLogradouroNumeroDne) {
          field.Name = "tipoLogradouroNumeroDne";
          field.Type = TType.String;
          field.ID = 10;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(TipoLogradouroNumeroDne);
          oprot.WriteFieldEnd();
        }
        if (__isset.stSemNumero) {
          field.Name = "stSemNumero";
          field.Type = TType.Bool;
          field.ID = 11;
          oprot.WriteFieldBegin(field);
          oprot.WriteBool(StSemNumero);
          oprot.WriteFieldEnd();
        }
        if (PontoReferencia != null && __isset.pontoReferencia) {
          field.Name = "pontoReferencia";
          field.Type = TType.String;
          field.ID = 12;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(PontoReferencia);
          oprot.WriteFieldEnd();
        }
        if (MicroArea != null && __isset.microArea) {
          field.Name = "microArea";
          field.Type = TType.String;
          field.ID = 13;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(MicroArea);
          oprot.WriteFieldEnd();
        }
        if (__isset.stForaArea) {
          field.Name = "stForaArea";
          field.Type = TType.Bool;
          field.ID = 14;
          oprot.WriteFieldBegin(field);
          oprot.WriteBool(StForaArea);
          oprot.WriteFieldEnd();
        }
        oprot.WriteFieldStop();
        oprot.WriteStructEnd();
      }
      finally
      {
        oprot.DecrementRecursionDepth();
      }
    }

    public override string ToString() {
      StringBuilder __sb = new StringBuilder("EnderecoLocalPermanenciaThrift(");
      bool __first = true;
      if (Bairro != null && __isset.bairro) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("Bairro: ");
        __sb.Append(Bairro);
      }
      if (Cep != null && __isset.cep) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("Cep: ");
        __sb.Append(Cep);
      }
      if (CodigoIbgeMunicipio != null && __isset.codigoIbgeMunicipio) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("CodigoIbgeMunicipio: ");
        __sb.Append(CodigoIbgeMunicipio);
      }
      if (Complemento != null && __isset.complemento) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("Complemento: ");
        __sb.Append(Complemento);
      }
      if (NomeLogradouro != null && __isset.nomeLogradouro) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("NomeLogradouro: ");
        __sb.Append(NomeLogradouro);
      }
      if (Numero != null && __isset.numero) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("Numero: ");
        __sb.Append(Numero);
      }
      if (NumeroDneUf != null && __isset.numeroDneUf) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("NumeroDneUf: ");
        __sb.Append(NumeroDneUf);
      }
      if (TelefoneContato != null && __isset.telefoneContato) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("TelefoneContato: ");
        __sb.Append(TelefoneContato);
      }
      if (TelefoneResidencia != null && __isset.telefoneResidencia) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("TelefoneResidencia: ");
        __sb.Append(TelefoneResidencia);
      }
      if (TipoLogradouroNumeroDne != null && __isset.tipoLogradouroNumeroDne) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("TipoLogradouroNumeroDne: ");
        __sb.Append(TipoLogradouroNumeroDne);
      }
      if (__isset.stSemNumero) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("StSemNumero: ");
        __sb.Append(StSemNumero);
      }
      if (PontoReferencia != null && __isset.pontoReferencia) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("PontoReferencia: ");
        __sb.Append(PontoReferencia);
      }
      if (MicroArea != null && __isset.microArea) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("MicroArea: ");
        __sb.Append(MicroArea);
      }
      if (__isset.stForaArea) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("StForaArea: ");
        __sb.Append(StForaArea);
      }
      __sb.Append(")");
      return __sb.ToString();
    }

  }

}
